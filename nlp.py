import streamlit as st
import streamlit as st1
import streamlit.components.v1 as stc

# File Processing Pkgs
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import docx2txt
from PIL import Image
from PyPDF2 import PdfFileReader
import pdfplumber


def read_pdf(file):
    pdfReader = PdfFileReader(file)
    count = pdfReader.numPages
    all_page_text = ""
    for i in range(count):
        page = pdfReader.getPage(i)
        all_page_text += page.extractText()

    return all_page_text

def main():
    st.title("RESUME SCREENING")
    menu = ["DocumentFiles", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    img = Image.open("C:/DATA/Programming/Python3.7/FirstProgram/HelloWorld/Cover.png")
    st.image(img)
    if choice == "DocumentFiles":
        st.subheader("Document Files Job Description :")
        docx_file = st.file_uploader("Job Description", type=['txt', 'docx', 'pdf'])
        st.subheader("Document Files Resume : ")
        li=[]
        docx_file1 = st.file_uploader("Resume-1", type=['txt', 'docx', 'pdf'])
        st.subheader("Document Files Resume : ")
        docx_file2 = st.file_uploader("Resume-2", type=['txt', 'docx', 'pdf'])
        st.subheader("Document Files Resume : ")
        docx_file3 = st.file_uploader("Resume-3", type=['txt', 'docx', 'pdf'])
        st.subheader("Document Files Resume : ")
        docx_file4 = st.file_uploader("Resume-4", type=['txt', 'docx', 'pdf'])
        st.subheader("Document Files Resume : ")
        docx_file5 = st.file_uploader("Resume-5", type=['txt', 'docx', 'pdf'])
        st.subheader("Document Files Resume : ")
        docx_file6 = st.file_uploader("Resume-6", type=['txt', 'docx', 'pdf'])
        st.subheader("Document Files Resume : ")
        docx_file7 = st.file_uploader("Resume-7", type=['txt', 'docx', 'pdf'])
        st.subheader("Document Files Resume : ")
        docx_file8 = st.file_uploader("Resume-8", type=['txt', 'docx', 'pdf'])
        st.subheader("Document Files Resume : ")
        docx_file9 = st.file_uploader("Resume-9", type=['txt', 'docx', 'pdf'])
        st.subheader("Document Files Resume : ")
        docx_file10 = st.file_uploader("Resume-10", type=['txt', 'docx', 'pdf'])
        li.extend([docx_file1,docx_file2,docx_file3,docx_file4,docx_file5,docx_file6,docx_file7,docx_file8,docx_file9,docx_file10])
        if st.button("Process"):
            if docx_file is not None:
                file_details = {"Filename": docx_file.name, "FileType": docx_file.type, "FileSize": docx_file.size}
                #st.write(file_details)
                if docx_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                    # Use the right file processor ( Docx,Docx2Text,etc)
                    job_description = docx2txt.process(docx_file)  # Parse in the uploadFile Class directory
                    st.write(job_description)
                    match=[]
                    st.write("------------------------------------------------------------------------------------------")
                    for i in range(10):
                        resume= docx2txt.process(li[i])
                        x=resume.split()[:2]
                        x=x[0]+" "+x[1]
                        content = [job_description, resume]
                        cv = CountVectorizer()
                        count_matrix = cv.fit_transform(content)
                        mat = cosine_similarity(count_matrix)
                        #st.write(mat)
                        st.write(x,'- Resume Matches by: ' + str(mat[1][0] * 100) + '%\n')
                        if mat[1][0]*100>=50:
                            match.append([round(mat[1][0]*100),x,i])
                    st.write("------------------------------------------------------------------------------------------")
                    st.write("------------------------------------------------------------------------------------------")
                    st.write("\n\nSelected Persons : ")
                    for i in match:
                        st.write(i[1],i[0],i[2]+1)






    else:
        st.subheader("About")
        st.info("Built with Streamlit")
        st.text("Resume screening is the process of identifying if a candidate qualifies ")
        st.text("for a job by matching the requirements of the role with the information ")
        st.text("on their resumes such as education, skills, certifications, experience, ")
        st.text("and achievements. Resume screening is crucial to determine whether a ")
        st.text("candidate moves to the next stage of the hiring process or not, especially ")
        st.text("in high-volume application scenarios.")


if __name__ == '__main__':
    main()