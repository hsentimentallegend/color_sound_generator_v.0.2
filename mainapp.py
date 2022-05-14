from nbformat import read
import streamlit as st
import st_03
import st_05upl

def main():
    with st.sidebar:
        st.title('Color Sound Generator')
        st.write('This is an application that converts the color RGB values of an image to sound.')
        st.write('you can select the mode Camera or upload')
        page = st.selectbox('', ('Camera mode', 'Upload mode'), )
        st.image('c-001.jpg')
        
        st.title('credit')
        st.write('developed by , directed by ')
        link = '[Website](https://www.mehatasentimentallegend.com/)'
        st.markdown(link, unsafe_allow_html=True)


    if page == 'Camera mode':
        st_03.render()
    elif page == 'Upload mode':
        st_05upl.render()


if __name__ == '__main__':
    main()



