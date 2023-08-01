import scrapy
import json

class TargetSpider(scrapy.Spider):
    name = "target"
    allowed_domain = ["target.com"]
    start_urls = ['https://redsky.target.com/redsky_aggregations/v1/web/pdp_client_v1?key=9f36aeafbe60771e321a7cc95a78140772ab3e96&tcin=79344798&is_bot=false&store_id=1478&pricing_store_id=1478&has_pricing_store_id=true&has_financing_options=true&visitor_id=0189AD6FECC102018D61C0AA40986573&has_size_context=true&latitude=18.500&longitude=73.960&zip=41230&state=MH&skip_personalized=true&channel=WEB&page=%2Fp%2Fundefined',
                  'https://redsky.target.com/redsky_aggregations/v1/web/pdp_client_v1?key=9f36aeafbe60771e321a7cc95a78140772ab3e96&tcin=13493042&is_bot=false&pricing_store_id=1478&has_pricing_store_id=true&has_financing_options=true&latitude=18.500&longitude=73.960&zip=41230&state=MH&skip_personalized=true&channel=WEB&page=%2Fp%2Fundefined',
                  'https://redsky.target.com/redsky_aggregations/v1/web/pdp_client_v1?key=9f36aeafbe60771e321a7cc95a78140772ab3e96&tcin=79405895&is_bot=false&store_id=1478&pricing_store_id=1478&has_pricing_store_id=true&has_financing_options=true&visitor_id=0189AD2F11060201A2DF35A10EF9CF2A&has_size_context=true&latitude=40.81679916&longitude=-73.04507446&zip=00501&state=NY&skip_personalized=true&channel=WEB&page=%2Fp%2FA-79405895']

    def parse(self,response):
        json_data = json.loads(response.body)
        product_details = json_data.get('data',{})
        # print(product_details)
        yield {
            'url' : product_details.get('product',{}).get('item',{}).get('enrichment',{}).get('buy_url',''),
            'tcin': product_details.get('product',{}).get('tcin',''),
            'currency': 'USD',
            'price_amount': product_details.get('product',{}).get('price',{}).get('current_retail',''),
            'price_amount': product_details.get('product',{}).get('price',{}).get('current_retail',''),
            'description': product_details.get('product',{}).get('item',{}).get('product_description',{}).get('downstream_description',''),
            'bullets': product_details.get('product',{}).get('item',{}).get('product_description',{}).get('soft_bullets',{}).get('bullets',[]),
            'ingredients': product_details.get('product',{}).get('item',{}).get('enrichment',{}).get('nutrition_facts',{}).get('value_prepared_list',[{}])[0].get('nutrients',''),
            'specs': product_details.get('product',{}).get('item',{}).get('product_description',{}).get('bullet_descriptions',[]),
            'features': product_details.get('product',{}).get('item',{}).get('product_description',{}).get('bullet_descriptions',[]),

        }