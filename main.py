# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 10:10:07 2023

@author: gis
"""
import streamlit as st
import base64
from pathlib import Path
import tempfile
from PIL import Image

st.set_page_config(page_title="Health GIS", layout="wide")

#pdffile = open('最终版本-健康GIS研讨会2023一号通知.pdf', 'rb')


image1 = Image.open('展板.jpg')
image2 = Image.open('易拉宝.jpg')
image3 = Image.open('正文题图.png')
image12 = Image.open('现场图片1.jpg')
image626 = Image.open('626.jpg')
image627 = Image.open('627.jpg')
image628 = Image.open('628.jpg')
image629 = Image.open('629.jpg')
imagemap = Image.open('地图.jpg')

logoimage = Image.open('网站背景长.jpg')
st.image(logoimage,caption=' ',use_column_width=True)
    
tab1,tab2,tab4,tab5,tab6 = st.tabs(["本届会议概览","会议通知及日程","历届会议信息","会议报名","参会地图"])

tab11,tab12 = tab1.columns(2)
#tab1.markdown('',unsafe_allow_html=True)
tab11.markdown("""<span>在由于新冠疫情暂时停办三年之后，第七届“地理信息技术在公共卫生领域的应用”讲习班今年于6月27日29日在上海恢复举办并取得圆满成功。这一由国际华人地理信息科学协会（CPGIS）主办的讲习班系列已经举办了七届。自2016年第三届起，该讲习班由华东师范大学地理科学学院承办。</span>""",unsafe_allow_html=True)
tab11.markdown("""<span>今年有近130名同仁报名参与讲习班，创历史新高。这些同仁来自17个省、直辖市、特别行政区、自治区，39家单位，包括高校、科研院所、政府职能部门，参会者背景以公共卫生、地理、城市规划居多。</span>""",unsafe_allow_html=True)
tab11.markdown("""<span>今年共有18位来自国内外的老师为讲习班提供了专题讲座或软件培训，涉及健康地理、健康GIS的各个方面，既展现了这一领域最热门的题目，最前沿的探索，最崭新的成果，也普及了这一领域的基础知识和基本技能。尤其是本次讲习班在正式开始之前，增加了一天的GIS软件基础培训，深受参会者的欢迎。讲习班的具体内容见《会议通知》附件2。</span>""",unsafe_allow_html=True)
tab11.markdown("""<span>本次讲习班特别邀请到国际著名学者，英国社会科学院院士，美国地理学家协会杰出学术成就奖获得者，香港中文大学的关美宝教授到场。关教授的“面向健康研究的大数据与地理空间技术”的精彩报告将讲习班的学术水平带到了一个新层次。</span>""",unsafe_allow_html=True)
tab11.markdown("""<span>在会后的问卷调查中，参会的同仁对讲习班的内容、形式、组织给与了热烈反馈，为进一步办好这个讲习班提供宝贵的意见和建议，如增加讨论和互动环节的时间等。</span>""",unsafe_allow_html=True)
tab11.markdown("""<span>本次协办单位包括中国地理学会健康地理专业委员会、中国地理学会地理模型与地理信息分析专业委员会、中国地理学会环境地理专业委员会；承办单位包括华东师范大学地理科学学院、地理信息科学教育部重点实验室、自然资源部超大城市自然资源时空大数据分析应用重点实验室、联合国可持续发展大数据国际研究中心分中心CBAS-ECNU；特别鸣谢上海地听信息科技有限公司、Esri中国信息科技有限公司上海分公司的支持。</span>""",unsafe_allow_html=True)

tab12.image(image12,caption=' ',width=800,use_column_width=False)

tab2.download_button("会议通知pdf下载", '最终版本-健康GIS研讨会2023一号通知.pdf', file_name="2023健康GIS会议一号通知.pdf",mime='application/pdf', key=None, help=None, on_click=None, args=None, kwargs=None)
tab2.download_button("会议日程pdf下载", '最终版本-健康GIS研讨会2023一号通知.pdf', file_name="2023健康GIS会议日程.pdf",mime='application/pdf', key=None, help=None, on_click=None, args=None, kwargs=None)

tab2.image(image3,caption=' ',width=1200,use_column_width=False)
tab2.markdown('<i class="material-icons">近年来，环境污染、爆发性传染病等公共卫生健康问题已成为各级政府、科研机构和公众关注的焦点。地理信息和空间分析技术为这些问题的解决提供了一个新的研究工具，目前已广泛应用于各个领域。为培养我国公共卫生与地理信息技术复合型人才，国际华人地理信息科学协会（The International Association of Chinese Professionals in Geographic Information Sciences,简称CPGIS）携手中国地理学会健康地理专业委员会、中国地理学会地理模型与地理信息分析专业委员会、中国地理学会环境地理专业委员会，秉持“以交流促进步，以沟通促学习”的理念，于2023年6月26 - 29日在华东师范大学举办第七届“地理信息和空间分析技术在公共卫生健康领域的应用”研讨会。本次研讨会拟采用线上线下结合的方式，邀请相关领域有较高建树的华人学者就地理信息和空间分析技术的基本原理、方法及其在公共卫生健康领域的实际应用进行讲座介绍、讨论和上机培训。</i>',unsafe_allow_html=True)
tab2.markdown('<i class="material-icons">我们诚挚邀请医疗卫生学术团体、研究机构的学术骨干，各级疾病预防控制中心、医疗卫生单位的工作人员，全国各高等院校医学、地理学、环境科学等相关专业的教师和研究生、高年级本科生，以及其他有志于“健康”领域研究的人员加入！期待大家的到来！</i>',unsafe_allow_html=True)
tab2.markdown('<i class="material-icons">主办：国际华人地理信息科学协会</i>',unsafe_allow_html=True)
tab2.markdown('<i class="material-icons">协办：中国地理学会健康地理专业委员会、中国地理学会地理模型与地理信息分析专业委员会、中国地理学会环境地理专业委员会</i>',unsafe_allow_html=True)
tab2.markdown('<i class="material-icons">承办：华东师范大学地理科学学院、地理信息科学教育部重点实验室、自然资源部超大城市自然资源时空大数据分析应用重点实验室、联合国可持续发展大数据国际研究中心分中心CBAS-ECNU</i>',unsafe_allow_html=True)

h2=tab2.header("一、研讨会内容及主讲专家")
tab2.markdown('<style>h2{font-size:25px;}</style>',unsafe_allow_html=True)

h4=tab2.caption("研讨会主要分为论坛及培训两部分，其中培训部分又分为健康GIS专业软件培训与Geoscene Pro GIS基础软件培训。")
tab2.markdown('<style>h4{color: rgb(0, 0, 0);}{font-size:15px;}</style>',unsafe_allow_html=True)

h3=tab2.subheader("（一）论坛内容及主讲学者")
tab2.markdown('<style>h3{font-size:20px;}</style>',unsafe_allow_html=True)

tab2.caption("论坛分为讲座及讨论两部分。")
tab2.caption("1.讲座")
tab2.caption("邀请知名学者介绍地理信息科学与技术在流行病学、环境健康、医疗服务资源配置等领域的应用。主讲学者包括（以下按姓氏笔画排列）：")

tab2.text("王法辉：路易斯安那州立大学Cyril & Tutta Vetter Alumni命名教授")
tab2.text("王劲峰：中国科学院地理科学与资源研究所/资源与环境信息系统国家重点实验室研究员")
tab2.text("关美宝：香港中文大学地理与资源管理学卓敏教授")
tab2.text("刘　艳：澳大利亚昆士兰大学地理信息科学专业讲席教授")
tab2.text("杨林生：中国科学院地理科学与资源研究所研究员")
tab2.text("邱　方：美国达拉斯得克萨斯大学地理空间信息科学系教授")
tab2.text("邹　滨：中南大学地球科学与信息物理学院教授")
tab2.text("林　戈：香港科技大学（广州）城市治理与设计学域教授")
tab2.text("施　迅：美国达特茅斯学院地理系教授")
tab2.text("徐　冰：清华大学地球系统科学系教授")
tab2.text("黄　波：香港中文大学伟伦讲座教授")
tab2.text("屠　威：美国南佐治亚大学地理学和地理信息科学系教授")
tab2.text("曹　凯：华东师范大学地理科学学院教授")
tab2.text("程　杨：北京师范大学地理科学学部地理学院副教授")
tab2.text("鲍曙明：美国中国数据研究所研究员")

tab2.caption("2.讨论")
tab2.caption("邀请参加讲座的学者以讨论形式就科研及业务部门关心的若干问题进行深入探讨，与大家开展广泛交流。也欢迎大家带着实际数据或问题来参与讨论。")

tab2.subheader("（二）培训内容及授课师资")
tab2.caption("培训采用上机实习的方式，普及有关理论方法和软件技术，同时探讨在中国具体环境下的应用。需要学员对GIS有基本的了解和兴趣。培训内容分为以下两部分：")
tab2.caption("培训 I ：健康GIS专业软件培训，包括ArcHealth软件包在疾病制图中的应用、健康风险归因地理探测器与疾病制图、2SFCA扩大版（加i2SFCA & 2SVCA)。")
tab2.caption("培训 II ：Geoscene Pro基础及其空间分析工具在公共卫生健康领域的应用。")

tab2.text("指导老师包括：")
tab2.text("施　迅：美国达特茅斯学院地理系教授")
tab2.text("李美芳：美国达特茅斯学院研究员")
tab2.text("徐成东：中国地理科学与资源研究所/资源与环境信息系统国家重点实验室副研究员")
tab2.text("姚申君：华东师范大学地理科学学院副教授")

tab2.text（"具体内容详见下载文件"）

tab2.header("二、时间及地点")
tab2.text("论坛时间：2023年6月27-29日上午8:30-下午2:15（6月26日下午开始报到注册）")
tab2.text("培训I时间：2023年6月27-29日下午2:30-5:00")
tab2.text("培训II时间：2023年6月26日上午9:00-下午5:00（6月26日上午开始报到注册）")
tab2.text("地点：华东师范大学闵行校区（上海市东川路500号）")

tab4.subheader("敬请期待")

tab5.subheader("今年的会议已经落下帷幕，期待明年再会!")
file = tab5.file_uploader("选择待上传的报名表pdf文件", type=['pdf'])
if file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        fp = Path(tmp_file.name)
        fp.write_bytes(file.getvalue())
        with open(tmp_file.name, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" ' \
                      f'width="800" height="1000" type="application/pdf">'
        tab5.markdown(pdf_display, unsafe_allow_html=True)

tab6.write("华东师范大学闵行校区地图如下：")
tab6.image(imagemap,caption=' ',width=900,use_column_width=False)


