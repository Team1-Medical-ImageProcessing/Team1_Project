import streamlit as st
from PIL import Image, ImageOps, ImageFilter

import numpy as np


def process_image(upload, name, col1, col2, col3, col4):
    image = Image.open(upload)
    col1.write("Input")
    col1.image(image)

    output = image.convert('L')
    col2.write("Output 1 : Grayscale")
    col2.image(output)

    output = ImageOps.equalize(output)
    col3.write("Output 2 : Histogram Equalization")
    col3.image(output)

    col4.write("Output 3 : Lowpass Gaussian Filter")
    output = image.filter(ImageFilter.GaussianBlur(50))
    col4.image(output)

    st.session_state[f"{name}_image"] = upload


def member_page(name):
    st.write(f"### {name}'s page")
    st.write(f"**{name}**")

    my_upload = st.sidebar.file_uploader("Image Upload", type=["png", "jpg", "jpeg"], key=name)

    col1, col2, col3, col4 = st.columns(4)

    if my_upload is not None:
        process_image(upload=my_upload, name=name, col1=col1, col2=col2, col3=col3, col4=col4)

    elif f"{name}_image" in st.session_state:
        process_image(upload=st.session_state[f"{name}_image"], name=name, col1=col1, col2=col2, col3=col3, col4=col4)

    elif my_upload is None:
        process_image(upload="./gr.jpeg", name=name, col1=col1, col2=col2, col3=col3, col4=col4)


st.set_page_config(layout="wide", page_title="1팀")
st.sidebar.write("## Sidebar")

menu = st.sidebar.radio(
    "Choose the menu",
    ("main page", "Result")
)

if menu == "main page":
    st.write("# 1팀")

    st.write("## 💡 Title")
    st.write(
        "*A Novel Subpixel Registration for Dual-Layer Detector Based on the Amplitude Response and Improved Low-Dose X-Ray Image*")

    st.write("## 📘 Background")

    st.write(
        """
        현대 의료에서 방사선 이미지를 사용한 검사는 빠르고 효율적인 진단 수단으로 질병의 조기 발견과 치료에 필수적이다. 그러나 반복적인 방사선의 노출로 인한 누적 방사선 피폭 위험이 증가함에 따라, 저선량으로 높은 품질의 방사선 이미지를 획득하는 디텍터와 영상처리 방법의 개발은 진단의 정확성은 유지하면서도 환자의 피폭량을 줄이는데 있어 매우 중요하다[1].

        방사선 디텍터에서 저선량으로도 좋은 품질의 이미지를 획득하기 위해서는 디텍터의 양자 효율을 증가시켜야 한다. 이를 위해 본 프로젝트에서는 두 개의 방사선 디텍터를 적층하여 제작한 이중층 디텍터(dual-layer detector)를 사용해 잡음이 개선된 저선량 이미지를 획득한다[2]. 이러한 이중층 디텍터는 기존 단일층 디텍터 또는 이중층 디텍터의 상부층에서 버려지는 광자까지 하부층에서 모두 사용이 가능해 광자 효율을 높일 수 있다[3].

        저선량 이미지를 획득하고자 본 프로젝트에서는 이중층 디텍터에서 획득한 영상들의 볼록조합이미지(convex combination image, CCI)를 사용한다. 최적의 조합계수일 때 신호대잡음비(signal to noise ratio, SNR)가 단일층 디텍터에 비하여 더 우수한 이미지를 획득할 수 있다. 즉, 저선량에서도 좋은 SNR을 가지는 이미지 획득이 가능하다[3].

        또한 SNR 스펙트럼은 디텍터의 검출양자효율 (detective quantum efficiency, DQE)의 제곱근에 비례하므로 높은 DQE성능을 보이는 디텍터는 개선된 저선량 이미지의 획득이 가능하다[3].

        이러한 이중층 디텍터는 두 개의 디텍터 층을 적층하여 생산하는데, 생산공정에 의해 두 층간에 수평과 수직 방향으로 서브픽셀 단위의 부정합이 존재한다. 따라서 이렇게 부정합이 있는 두 층에서 획득한 이미지들에도 부정합이 존재하며, 이들간의 매우 정밀한 서브픽셀 정합은 이중층 디텍터를 활용하여 좋은 품질의 저선량 이미지를 획득하는 데 매우 중요하다.

        따라서 본 프로젝트에서는 먼저 주어진 참고문헌에 따라 이중층 디텍터에서 획득한 영상의 고정밀 정합을 위한 새로운 개념의 서브픽셀 정합 방법을 구현한다. 이후 이중층 디텍터에서 획득한 영상의 CCI로 개선된 잡음 특성을 가지는 높은 품질의 저선량 방사선 이미지를 생성한다.
        """
    )

    st.image("영상처리 팀페이지 이미지.webp",
             caption="Figure 1. 이중층 디텍터에서 획득한 이미지의 서브픽셀 정합과 CCI를 통한 저선량 방사선 이미징 알고리즘")

    st.write("## ⭐ Purpose")
    st.write(
        """
        본 프로젝트에서는 개선된 저선량 방사선 이미지를 얻기 위한 과정을 다음과 같이 제안한다.

        1. 참고문헌에 기반하여 정밀한 서브픽셀 정합을 위한 새로운 개념의 서브픽셀 정합 알고리즘 구현
        2. 이중층 디텍터(dual-layer detector)에서 얻은 상부 및 하부 이미지에 구현한 서브픽셀 정합 알고리즘을 적용하여 하부 이미지를 정렬하고, 정렬된 이미지들간의 볼록조합이미지(convex combination image)획득
        3. 정렬한 이미지를 이용해 만든 볼록조합이미지를 통해 저선량 환경에서 획득한 x-ray이미지에서의 잡음 개선을 진행
        4. 개선된 잡음을 수치해석 및 몬테-카를로 시뮬레이션을 통해 검증함
        """
    )

    st.write("## 🍀 Plans")
    st.write(
        """
        - Experiment subject selection, background research, and experiment algorithm design
        - Algorithm implementation and experiment progress, data collection (using MATLAB)
        - Performance comparison with traditional methods (imregister, MATLAB), algorithm optimization
        - Apply to CCI of actual x-ray image pair, and improve noise of CCI
        - Verify the improved noise at CCI using numerical analysis and monte-carlo simulation
        - Organize results and write a report
        """
    )

    st.write("## 👥 Members")
    st.write(
        """
        | Name | Major | Contact |
        | --- | --- | --- |
        | 강대홍 | 바이오메디컬공학부 | rkdeoghd99@hufs.ac.kr |
        | 송윤주 | 바이오메디컬공학부 | shing1209@hufs.ac.kr |
        | 이나림 | 바이오메디컬공학부 | nadool0216@hufs.ac.kr |
        | 이다연 (팀장) | 전자공학과 | plant3032@gmail.com |
        | 허은재 | 전자공학과 | heoeunjae0825@gmail.com |

        """
    )

# elif menu == "team member_radio":
#     team_member = st.sidebar.radio(
#         "Members",
#         ("Team1", "강대홍", "송윤주", "이나림", "이다연", "허은재")
#     )
#     member_page(team_member)

elif menu == "Result":
    team_member = st.sidebar.selectbox(
        "Members",
        ("Team1", "강대홍", "송윤주", "이나림", "이다연", "허은재")
    )
    member_page(team_member)