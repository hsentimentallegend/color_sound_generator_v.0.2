import streamlit as st
import st_05upl
import st_03
import St_06_rgb

def main():
    with st.sidebar:
        st.title('Color Sound Generator')
        st.write('This is an application that converts the color RGB values of an image to sound.')
        st.write('you can select the mode Camera or upload')
        page = st.selectbox('', ('Normal mode', 'Mini Cam mode','RGB 3 tone mode'), )
        st.image('c-001.jpg')
        
        st.title('credit')
        st.write('developed by Hiroshi Mehata, directed by Hiroshi Mehata')
        link = '[Website](https://www.mehatasentimentallegend.com/)'
        st.markdown(link, unsafe_allow_html=True)
        
        st.title('concept')
        st.write('This app was created for the sound installation of the Hiroshi Mehata solo exhibition - Color Cleanser (2023).')
        st.write('Take a photo of the paintings in the exhibition space or the venue. The sound will be created from the color values contained in the photo.')
        st.write('Play that sound at the venue and be a part of the music at the venue.')


    if page == 'Normal mode':
        st_05upl.render()
    elif page == 'Mini Cam mode':
        st_03.render()
    elif page == 'RGB 3 tone mode':
        St_06_rgb.render()

if __name__ == '__main__':
    main()



