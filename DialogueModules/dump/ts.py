import translators as ts

wyw_text = '季姬寂，集鸡，鸡即棘鸡。棘鸡饥叽，季姬及箕稷济鸡。'
chs_text = '季姬感到寂寞，罗集了一些鸡来养，鸡是那种出自荆棘丛中的野鸡。野鸡饿了唧唧叫，季姬就拿竹箕中的谷物喂鸡。'

# input languages
print(ts.google(wyw_text))  # default: from_language='auto', to_language='en'

# ## output language_map
# print(ts._google.language_map)
#
# # professional field
# print(ts.alibaba(wyw_text, professional_field='general'))  # ("general","message","offer")
# print(ts.baidu(wyw_text, professional_field='common'))  # ('common','medicine','electronics','mechanics')
#
# # requests
# print(ts.youdao(wyw_text, sleep_seconds=5, proxies={}))
#
# # host service
# print(ts.google(wyw_text, if_use_cn_host=True))
# print(ts.bing(wyw_text, if_use_cn_host=False))