# -*- coding: utf-8 -*-
import scrapy


class AnjukeSpider(scrapy.Spider):
    name = 'anjuke'
    allowed_domains = ['anjuke.com']
    start_urls = ['https://m.anjuke.com/sh/']
    headers = {

        'user-agent':'Alcatel-BH4/1.0 UP.Browser/6.2.ALCATEL MMP/1.0 ',
        'cookie' : 'als=0; _ga=GA1.2.778122783.1512476933; isp=true; aQQ_ajkguid=47F0782C-1FBA-44D7-E85E-964CC0E5BF3F; 58tj_uuid=08f394fa-f500-4fe2-821e-c185eb205300; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1512476958,1513514122,1513562346; lps=http%3A%2F%2Fwww.anjuke.com%2F%3Fpi%3DPZ-baidu-pc-all-biaoti%7Chttp%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00fDgzw60Pj4U00PpAsjxEWkp00000PzE6db00000uNZ0jM.THvs_oeHEtY0UWdBmy-bIy9EUyNxTAT0T1dbryf3mhmknH0snjFbuhmL0ZRqPYnLfWfknjD3wjF7fYczPYuAwHbvPbcsf1DkP17arHc0mHdL5iuVmv-b5HnsPWbLrHRYPW6hTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8my4JIyV-QhPEUitOTAbqR7CVmh7GuZRVTAnVmyk_QyFGmyqYpfKWThnqnWRdrHR%26tpl%3Dtpl_10085_15730_11224%26l%3D1501802460%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E5%2525AE%252589%2525E5%2525B1%252585%2525E5%2525AE%2525A2-%2525E5%25259B%2525BD%2525E5%252586%252585%2525E9%2525A2%252586%2525E5%252585%252588%2525E6%252589%2525BE%2525E6%252588%2525BF%2525E5%2525B9%2525B3%2525E5%25258F%2525B0%2525EF%2525BC%25258C%2525E5%2525AE%252589%2525E5%2525BF%252583%2525E6%25258C%252591%2526xp%253Did%28%252522m2a82b662%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D219%26wd%3D%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%26issp%3D1%26f%3D3%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26oq%3D%2525E9%252593%2525BE%2525E5%2525AE%2525B6%26inputT%3D5209%26prefixsug%3DANJU%26rsp%3D0; twe=2; sessid=C182E734-B7CB-0D00-A4C7-759C37703D8E; _gid=GA1.2.1473221272.1513930537; ctid=11; ajk_member_captcha=e9e95513f140a76a62fa7040ce469d01; propertys=hr7jcp-p1cyf3_hq3va8-p1cttn_hq0qtq-p1csbx_h20s3r-p13usm_h7z732-p13umd_; init_refer=https%253A%252F%252Fshanghai.anjuke.com%252F%253Fpi%253DPZ-baidu-pc-all-biaoti; new_uv=11; new_session=0; __xsptplus8=8.20.1513955686.1513957065.12%232%7Cbzclk.baidu.com%7C%7C%7C%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%7C%23%23tNXbDl0f23bMqI1CcDs9-nwmColHSHQ6%23',
        'referer' : 'https://www.anjuke.com/captcha-verify/?callback=shield&from=antispam&history=aHR0cHM6Ly9tLmFuanVrZS5jb20vc2gv'
    }
    def parse(self, response):
        li_list = response.xpath("//ul[@id='houselist-mod-new']/li")
        for li in li_list:
            item = {}
            item["house_title"] = li.xpath(".//div[@class='house-title']/a/text()").extract_first()
            item["house_pr2ice"] = li.xpath(".//span[@class='price-det']//text()").extract_first()
            item["house_price1"] = li.xpath(".//div[@class='pro-price']/span[2]/text()").extract_first()
            item["house_href"] = li.xpath(".//div[@class='house-title']/a/@href").extract_first()
            # print(item)
            yield scrapy.Request(
                item["house_href"],
                callback=self.parse_list,
                meta = {"item":item}
            )

        # 翻页
        next_url_temp = response.xpath("//a[@class='aNxt']/@href").extract_first()
        if next_url_temp is not None:
            print("*" * 100)
            yield scrapy.Request(
                next_url_temp,
                callback=self.parse,
            )

    def parse_list(self,response):
        pass
        # print(dir(response))
        # item = response.meta["item"]
        # item["house_aa"] = response.xpath("//p[@class='broker-mobile']/text()").extract_first()
        # yield item