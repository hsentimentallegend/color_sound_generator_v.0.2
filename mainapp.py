import streamlit as st
import st_05upl
import st_03
import St_06_rgb

def main():
    with st.sidebar:
        st.title('Color Sound Generator')
        st.write('This is an application that converts the color RGB values of an image to sound.')
        st.write('you can select the mode Camera or upload')
        page = st.selectbox('', ('Normal mode', 'Mini Cam mode'), )
        st.image('c-001.jpg')
        
        st.title('credit')
        st.write('developed by Hiroshi Mehata, directed by Hiroshi Mehata')
        link = '[Website](https://www.mehatasentimentallegend.com/)'
        st.markdown(link, unsafe_allow_html=True)


    if page == 'Normal mode':
        st_05upl.render()
    elif page == 'Mini Cam mode':
        st_03.render()
    elif page == 'RGB 3 tone mode':
        St_06_rgb.render()

if __name__ == '__main__':
    main()



