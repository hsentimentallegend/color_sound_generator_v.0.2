import streamlit as st
import cv2
import numpy as np
from synthesizer import Synthesizer, Waveform, Writer
from PIL import Image

def render():  
 st.title('Color Sound Generator_Master_Version_1.0_3 Tone Mode')

 uploaded_file=st.file_uploader("Take a Picture or Upload your Pic to Generate Sound", type=['png', 'jpg', 'jpeg'] )
 if uploaded_file is not None:
     image=Image.open(uploaded_file)
     img_array = np.array(image)
     bytes_data = uploaded_file.read()
     st.image(img_array,caption = 'your picture',use_column_width = True)

     #ダウンロードボタン処理
     with open ('test.jpg','wb') as file:   
      file.write(uploaded_file.getbuffer())
      with open('test.jpg', "rb") as file:
       st.download_button(
        label="Download your picture",
        data=file,
        file_name='colorcleanser.jpg',
        mime="application/octet-stream"
        )         

    
     
     # To read image file buffer with OpenCV:
     bytes_data = uploaded_file.getvalue()
     cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

     #スマホ画像の読み取り速度を上げるためここで画像サイズを10分の1へリサイズしている（改善の余地あるかも）
     dst = cv2.resize(cv2_img, dsize=None, fx=0.1, fy=0.1)

     height, width, ch = dst.shape

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
     st.write("frequencies are created according to the average of the RGB values",(int(total)))

     value=(int(b_ave))
     if value>1 and value <4: 
    # ここの説明は 音作り を参照
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
     # 一定音程の波形を生成する
      wave = synth.generate_constant_wave(frequency=195.998, length=5.0) #lengthは音の長さ
     # オーディオファイル出力用クラス
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 195.998hz!!!')
     
     elif value>4 and value <=8 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=195.998, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 195.998hz!!!')


     elif value>8 and value <=12 :
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=207.652, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 207.652hz!!!')
      
     elif value>12 and value <=16 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=207.652, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 207.652hz!!!')

     elif value>16 and value <=20:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=233.082, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 233.082hz!!!')
      
      
     elif value>20 and value <=24:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=233.082, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 233.082hz!!!')
      
     elif value>24 and value <=28:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=261.626, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 261.626hz!!!')
      
     elif value>28 and value <=32:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=261.626, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 261.626hz!!!')
     

     elif value>32 and value <=36:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=277.183, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 277.183hz!!!')
      
     elif value>36 and value <=40:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=277.183, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 277.183hz!!!')
      
      
     elif value>40 and value <=44:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=311.127, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 311.127hz!!!')
      
     elif value>44 and value <=48:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=311.127, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 311.127hz!!!')
      

     elif value>48 and value <=52:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=349.228, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 349.228hz!!!')
      
     elif value>52 and value <=56:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=349.228, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 349.228hz!!!')

     elif value>56 and value <=60:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=391.995, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 391.995hz!!!')
      
     elif value>60 and value <=64:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=391.995, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 391.995hz!!!')
      
     elif value>64 and value <=68 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=415.305, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 415.305hz!!!')


     elif value>68 and value <=72 :
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=415.305, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 415.305hz!!!')
      
     elif value>72 and value <=76 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=466.164, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 466.164hz!!!')

     elif value>76 and value <=80:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=466.164, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 466.164hz!!!')
      
      
     elif value>80 and value <=84:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=523.251, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 523.251hz!!!')
      
     elif value>84 and value <=88:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=523.251, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 523.251hz!!!')
      
     elif value>88 and value <=92:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=554.365, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 554.365hz!!!')
     

     elif value>92 and value <=96:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=554.365, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 554.365hz!!!')
      
     elif value>96 and value <=100:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=622.254, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 622.254hz!!!')
      
      
     elif value>100 and value <=104:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=622.254, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 622.254hz!!!')
      
     elif value>104 and value <=108:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=698.456, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 698.456hz!!!')
      

     elif value>108 and value <=112:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=698.456, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 698.456hz!!!')
      
     elif value>112 and value <=116:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=783.991, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 783.991hz!!!')

     elif value>116 and value <=120:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=783.991, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 783.991hz!!!')
      
     elif value>120 and value <=124:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=830.609, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 830.609hz!!!')
      
     elif value>124 and value <=128 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=830.609, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 830.609hz!!!')


     elif value>128 and value <=132 :
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=932.328, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 932.328hz!!!')
      
     elif value>132 and value <=136 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=932.328, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 932.328hz!!!')

     elif value>136 and value <=140:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1046.502, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1046.502hz!!!')
      
      
     elif value>140 and value <=144:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1046.502, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1046.502hz!!!')
      
     elif value>144 and value <=148:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1108.731, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1108.731hz!!!')
      
     elif value>148 and value <=152:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1108.731, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1108.731hz!!!')
     

     elif value>152 and value <=156:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1244.508, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1244.508hz!!!')
      
     elif value>156 and value <=160:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1244.508, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1244.508hz!!!')
      
      
     elif value>160 and value <=164:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1396.913, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1396.913hz!!!')
      
     elif value>164 and value <=168:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1396.913, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1396.913hz!!!')
      

     elif value>168 and value <=172:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1567.982, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1567.982hz!!!')
      
     elif value>172 and value <=176:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1567.982, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1567.982hz!!!')

     elif value>176 and value <=180:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1661.219, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1661.219hz!!!')
      
     elif value>180 and value <=184:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1661.219, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1661.219hz!!!')
      
     elif value>184 and value <=188 :
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1864.655, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1864.655hz!!!')


     elif value>188 and value <=192 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1864.655, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1864.655hz!!!')
      
     elif value>192 and value <=196 :
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2093.005, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 2093.005hz!!!')

     elif value>196 and value <=200:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2093.005, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 2093.005hz!!!')
      
      
     elif value>200 and value <=204:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2217.461, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 2217.461hz!!!')
      
     elif value>204 and value <=208:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2217.461, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 2217.461hz!!!')
      
     elif value>208 and value <=212:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2489.016, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 2489.016hz!!!')
     

     elif value>212 and value <=216:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2489.016, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 2489.016hz!!!')
      
     elif value>216 and value <=220:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2793.826, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 2793.826hz!!!')
      
      
     elif value>220 and value <=224:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2793.826, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 2793.826hz!!!')
      
     elif value>224 and value <=228:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=3135.963, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 3135.963hz!!!')
      

     elif value>228 and value <=232:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=3135.963, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 3135.963hz!!!')
      
     elif value>232 and value <=236:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=3322.438, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 3322.438hz!!!')

     elif value>236 and value <=240:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=3322.438, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 3322.438hz!!!')
      
     elif value>240 and value <=244:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=3729.31, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 3729.31hz!!!')
      
      
     elif value>244 and value <=248:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=3729.31, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 3729.31hz!!!')
      
     elif value>248 and value <=252:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=4186.009, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 4186.009hz!!!')
      
      
     else : 
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=4186.009, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 4186.009hz!!!')


     audio_file = open('sine.wav', 'rb')
     audio_bytes = audio_file.read()

     st.audio(audio_bytes, format='audio/ogg')
     st.write("B color average Value",(int(b_ave)))

     # ここからg
     
     value=(int(g_ave))
     if value>1 and value <4: 
    # ここの説明は 音作り を参照
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
     # 一定音程の波形を生成する
      wave = synth.generate_constant_wave(frequency=195.998, length=5.0) #lengthは音の長さ
     # オーディオファイル出力用クラス
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 195.998hz!!!')
     
     elif value>4 and value <=8 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=195.998, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 195.998hz!!!')


     elif value>8 and value <=12 :
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=207.652, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 207.652hz!!!')
      
     elif value>12 and value <=16 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=207.652, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 207.652hz!!!')

     elif value>16 and value <=20:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=233.082, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 233.082hz!!!')
      
      
     elif value>20 and value <=24:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=233.082, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 233.082hz!!!')
      
     elif value>24 and value <=28:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=261.626, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 261.626hz!!!')
      
     elif value>28 and value <=32:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=261.626, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 261.626hz!!!')
     

     elif value>32 and value <=36:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=277.183, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 277.183hz!!!')
      
     elif value>36 and value <=40:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=277.183, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 277.183hz!!!')
      
      
     elif value>40 and value <=44:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=311.127, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 311.127hz!!!')
      
     elif value>44 and value <=48:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=311.127, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 311.127hz!!!')
      

     elif value>48 and value <=52:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=349.228, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 349.228hz!!!')
      
     elif value>52 and value <=56:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=349.228, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 349.228hz!!!')

     elif value>56 and value <=60:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=391.995, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 391.995hz!!!')
      
     elif value>60 and value <=64:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=391.995, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 391.995hz!!!')
      
     elif value>64 and value <=68 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=415.305, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 415.305hz!!!')


     elif value>68 and value <=72 :
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=415.305, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 415.305hz!!!')
      
     elif value>72 and value <=76 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=466.164, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 466.164hz!!!')

     elif value>76 and value <=80:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=466.164, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 466.164hz!!!')
      
      
     elif value>80 and value <=84:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=523.251, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 523.251hz!!!')
      
     elif value>84 and value <=88:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=523.251, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 523.251hz!!!')
      
     elif value>88 and value <=92:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=554.365, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 554.365hz!!!')
     

     elif value>92 and value <=96:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=554.365, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 554.365hz!!!')
      
     elif value>96 and value <=100:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=622.254, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 622.254hz!!!')
      
      
     elif value>100 and value <=104:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=622.254, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 622.254hz!!!')
      
     elif value>104 and value <=108:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=698.456, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 698.456hz!!!')
      

     elif value>108 and value <=112:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=698.456, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 698.456hz!!!')
      
     elif value>112 and value <=116:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=783.991, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 783.991hz!!!')

     elif value>116 and value <=120:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=783.991, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 783.991hz!!!')
      
     elif value>120 and value <=124:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=830.609, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 830.609hz!!!')
      
     elif value>124 and value <=128 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=830.609, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 830.609hz!!!')


     elif value>128 and value <=132 :
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=932.328, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 932.328hz!!!')
      
     elif value>132 and value <=136 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=932.328, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 932.328hz!!!')

     elif value>136 and value <=140:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1046.502, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1046.502hz!!!')
      
      
     elif value>140 and value <=144:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1046.502, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1046.502hz!!!')
      
     elif value>144 and value <=148:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1108.731, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1108.731hz!!!')
      
     elif value>148 and value <=152:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1108.731, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1108.731hz!!!')
     

     elif value>152 and value <=156:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1244.508, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1244.508hz!!!')
      
     elif value>156 and value <=160:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1244.508, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1244.508hz!!!')
      
      
     elif value>160 and value <=164:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1396.913, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1396.913hz!!!')
      
     elif value>164 and value <=168:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1396.913, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1396.913hz!!!')
      

     elif value>168 and value <=172:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1567.982, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1567.982hz!!!')
      
     elif value>172 and value <=176:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1567.982, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1567.982hz!!!')

     elif value>176 and value <=180:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1661.219, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1661.219hz!!!')
      
     elif value>180 and value <=184:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1661.219, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1661.219hz!!!')
      
     elif value>184 and value <=188 :
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1864.655, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1864.655hz!!!')


     elif value>188 and value <=192 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1864.655, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1864.655hz!!!')
      
     elif value>192 and value <=196 :
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2093.005, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 2093.005hz!!!')

     elif value>196 and value <=200:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2093.005, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 2093.005hz!!!')
      
      
     elif value>200 and value <=204:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2217.461, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 2217.461hz!!!')
      
     elif value>204 and value <=208:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2217.461, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 2217.461hz!!!')
      
     elif value>208 and value <=212:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2489.016, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 2489.016hz!!!')
     

     elif value>212 and value <=216:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2489.016, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 2489.016hz!!!')
      
     elif value>216 and value <=220:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2793.826, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 2793.826hz!!!')
      
      
     elif value>220 and value <=224:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2793.826, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 2793.826hz!!!')
      
     elif value>224 and value <=228:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=3135.963, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 3135.963hz!!!')
      

     elif value>228 and value <=232:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=3135.963, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 3135.963hz!!!')
      
     elif value>232 and value <=236:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=3322.438, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 3322.438hz!!!')

     elif value>236 and value <=240:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=3322.438, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 3322.438hz!!!')
      
     elif value>240 and value <=244:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=3729.31, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 3729.31hz!!!')
      
      
     elif value>244 and value <=248:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=3729.31, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 3729.31hz!!!')
      
     elif value>248 and value <=252:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=4186.009, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 4186.009hz!!!')
      
      
     else : 
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=4186.009, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 4186.009hz!!!')


     audio_file = open('sine.wav', 'rb')
     audio_bytes = audio_file.read()

     st.audio(audio_bytes, format='audio/ogg')
     st.write("G color average Value",(int(g_ave)))
     # ここからr
     
     value=(int(r_ave))
     if value>1 and value <4: 
    # ここの説明は 音作り を参照
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
     # 一定音程の波形を生成する
      wave = synth.generate_constant_wave(frequency=195.998, length=5.0) #lengthは音の長さ
     # オーディオファイル出力用クラス
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 195.998hz!!!')
     
     elif value>4 and value <=8 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=195.998, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 195.998hz!!!')


     elif value>8 and value <=12 :
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=207.652, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 207.652hz!!!')
      
     elif value>12 and value <=16 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=207.652, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 207.652hz!!!')

     elif value>16 and value <=20:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=233.082, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 233.082hz!!!')
      
      
     elif value>20 and value <=24:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=233.082, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 233.082hz!!!')
      
     elif value>24 and value <=28:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=261.626, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 261.626hz!!!')
      
     elif value>28 and value <=32:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=261.626, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 261.626hz!!!')
     

     elif value>32 and value <=36:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=277.183, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 277.183hz!!!')
      
     elif value>36 and value <=40:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=277.183, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 277.183hz!!!')
      
      
     elif value>40 and value <=44:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=311.127, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 311.127hz!!!')
      
     elif value>44 and value <=48:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=311.127, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 311.127hz!!!')
      

     elif value>48 and value <=52:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=349.228, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 349.228hz!!!')
      
     elif value>52 and value <=56:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=349.228, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 349.228hz!!!')

     elif value>56 and value <=60:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=391.995, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 391.995hz!!!')
      
     elif value>60 and value <=64:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=391.995, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 391.995hz!!!')
      
     elif value>64 and value <=68 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=415.305, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 415.305hz!!!')


     elif value>68 and value <=72 :
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=415.305, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 415.305hz!!!')
      
     elif value>72 and value <=76 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=466.164, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 466.164hz!!!')

     elif value>76 and value <=80:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=466.164, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 466.164hz!!!')
      
      
     elif value>80 and value <=84:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=523.251, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 523.251hz!!!')
      
     elif value>84 and value <=88:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=523.251, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 523.251hz!!!')
      
     elif value>88 and value <=92:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=554.365, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 554.365hz!!!')
     

     elif value>92 and value <=96:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=554.365, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 554.365hz!!!')
      
     elif value>96 and value <=100:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=622.254, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 622.254hz!!!')
      
      
     elif value>100 and value <=104:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=622.254, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 622.254hz!!!')
      
     elif value>104 and value <=108:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=698.456, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 698.456hz!!!')
      

     elif value>108 and value <=112:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=698.456, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 698.456hz!!!')
      
     elif value>112 and value <=116:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=783.991, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 783.991hz!!!')

     elif value>116 and value <=120:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=783.991, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 783.991hz!!!')
      
     elif value>120 and value <=124:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=830.609, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 830.609hz!!!')
      
     elif value>124 and value <=128 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=830.609, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 830.609hz!!!')


     elif value>128 and value <=132 :
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=932.328, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 932.328hz!!!')
      
     elif value>132 and value <=136 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=932.328, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 932.328hz!!!')

     elif value>136 and value <=140:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1046.502, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1046.502hz!!!')
      
      
     elif value>140 and value <=144:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1046.502, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1046.502hz!!!')
      
     elif value>144 and value <=148:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1108.731, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1108.731hz!!!')
      
     elif value>148 and value <=152:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1108.731, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1108.731hz!!!')
     

     elif value>152 and value <=156:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1244.508, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1244.508hz!!!')
      
     elif value>156 and value <=160:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1244.508, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1244.508hz!!!')
      
      
     elif value>160 and value <=164:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1396.913, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1396.913hz!!!')
      
     elif value>164 and value <=168:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1396.913, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1396.913hz!!!')
      

     elif value>168 and value <=172:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1567.982, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1567.982hz!!!')
      
     elif value>172 and value <=176:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1567.982, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1567.982hz!!!')

     elif value>176 and value <=180:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1661.219, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1661.219hz!!!')
      
     elif value>180 and value <=184:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1661.219, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1661.219hz!!!')
      
     elif value>184 and value <=188 :
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1864.655, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 1864.655hz!!!')


     elif value>188 and value <=192 :
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=1864.655, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 1864.655hz!!!')
      
     elif value>192 and value <=196 :
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2093.005, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 2093.005hz!!!')

     elif value>196 and value <=200:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2093.005, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 2093.005hz!!!')
      
      
     elif value>200 and value <=204:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2217.461, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 2217.461hz!!!')
      
     elif value>204 and value <=208:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2217.461, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 2217.461hz!!!')
      
     elif value>208 and value <=212:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2489.016, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 2489.016hz!!!')
     

     elif value>212 and value <=216:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2489.016, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 2489.016hz!!!')
      
     elif value>216 and value <=220:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2793.826, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 2793.826hz!!!')
      
      
     elif value>220 and value <=224:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=2793.826, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 2793.826hz!!!')
      
     elif value>224 and value <=228:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=3135.963, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 3135.963hz!!!')
      

     elif value>228 and value <=232:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=3135.963, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 3135.963hz!!!')
      
     elif value>232 and value <=236:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=3322.438, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 3322.438hz!!!')

     elif value>236 and value <=240:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=3322.438, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 3322.438hz!!!')
      
     elif value>240 and value <=244:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=3729.31, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 3729.31hz!!!')
      
      
     elif value>244 and value <=248:
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=3729.31, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 3729.31hz!!!')
      
     elif value>248 and value <=252:
      synth = Synthesizer(osc1_waveform=Waveform.sawtooth, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=4186.009, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate A 4186.009hz!!!')
      
      
     else : 
      synth = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
      wave = synth.generate_constant_wave(frequency=4186.009, length=5.0)
      writer = Writer()
      writer.write_wave("sine.wav", wave)

      st.write('## success to Generate B 4186.009hz!!!')


     audio_file = open('sine.wav', 'rb')
     audio_bytes = audio_file.read()

     st.audio(audio_bytes, format='audio/ogg')

     link = '[Share Picture with Instagram](https://www.instagram.com/)'
     st.markdown(link, unsafe_allow_html=True)
     st.write("R color average Value",(int(R_ave)))
