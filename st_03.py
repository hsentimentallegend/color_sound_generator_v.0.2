import streamlit as st
import cv2
import numpy as np
from synthesizer import Synthesizer, Waveform, Writer

def render():

 st.title('Color Sound Generator_Plot_Version_0.2')
 img_file_buffer = st.camera_input("Take a picture, and Generate Sound with the value of the Color",)
 if img_file_buffer is not None:

     with open ('test.jpg','wb') as file:   
       file.write(img_file_buffer.getbuffer())
     with open('test.jpg', "rb") as file:
       btn=st.download_button(
        label="Download Picture",
        data=file,
        file_name='colorcleanser.jpg',
        mime="application/octet-stream"
        )         
     # To read image file buffer with OpenCV:
     bytes_data = img_file_buffer.getvalue()
     cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
 
     height, width, ch = cv2_img.shape

     # 画素数 = 幅 * 高さ
     size = width * height
    # 情報表示 
     print("幅：", width)
     print("高さ：", height)
     print("チャンネル数:", ch)
     print("画素数:", size)   
     print("データ型：", cv2_img.dtype)
    
    # 1chずつ表示
     print("Bの画素値：\n", cv2_img[:,:,0])
     print("Gの画素値：\n", cv2_img[:,:,1])
     print("Rの画素値：\n", cv2_img[:,:,2])


       #数値の初期化
     l=0
     b_ave=0; g_ave=0; r_ave=0

     for i in range(height):
         for j in range(width):
             #画素値[0,0,0]（Black）を除外してピクセルの和とbgrの画素値の合計を計算する
             if(cv2_img[i,j,0] != 0 or cv2_img[i,j,1] != 0 or cv2_img[i,j,2] != 0 ):
                 l+=1     #対象となるピクセル数を計算する
                #対象となるピクセルの画素値の和を計算する
                 b_ave=b_ave+cv2_img[i,j,0]
                 g_ave=g_ave+cv2_img[i,j,1]
                 r_ave=r_ave+cv2_img[i,j,2]
             #画素値合計をピクセル数で除することでRGBの画素値の平均値を求める
         
     b_ave=b_ave/l
     g_ave=g_ave/l
     r_ave=r_ave/l

     print(np.round([b_ave, g_ave, r_ave]))

    

     total=((b_ave + g_ave + r_ave)/3) 
     st.write("over200 to Hi, 200-100 to Mid,under 100 to Low",(int(total)))

     value=(int(total))
     if value<200 and value >100: 
    # ここの説明は 音作り を参照
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
     # 一定音程の波形を生成する
      wave = synth.generate_constant_wave(frequency=800.0, length=5.0) #lengthは音の長さ
     # オーディオファイル出力用クラス
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate Mid!!!')




     elif value>200:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1200.0, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate Hi!!!')


     else : 
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=160.0, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate Low!!!')


     audio_file = open('sine.wav', 'rb')
     audio_bytes = audio_file.read()

     st.audio(audio_bytes, format='audio/ogg')

     link = '[Share Picture with Instagram](https://www.instagram.com/)'
     st.markdown(link, unsafe_allow_html=True)


