import os
import pathlib
import streamlit as st
from PIL import Image
import webbrowser

# 🛠️ 1. Configure a página
st.set_page_config(
    page_title="Portfólio - Paulo Roberto",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

SOCIAL_LINKS = {
    "LinkedIn": {"url": "https://www.linkedin.com/in/paulo-roberto/", "icon": "fab fa-linkedin"},
    "GitHub": {"url": "https://github.com/PaulodiasDeveloper", "icon": "fab fa-github"},
    "Instagram": {"url": "https://www.linkedin.com/in/paulo-roberto/", "icon": "fab fa-instagram"},
    "Youtube": {"url": "https://www.linkedin.com/in/paulo-roberto/", "icon": "fab fa-youtube"},
    "Twitter": {"url": "https://www.linkedin.com/in/paulo-roberto/", "icon": "fab fa-twitter"},
}

SKILLS = {
    "Frontend": ["React", "JavaScript (ES6+)", "HTML5 & CSS3", "Tailwind CSS"],
    "Backend": ["Python & Django", "FastAPI & Flask", "RESTful APIs", "PostgreSQL & MongoDB"],
    "DevOps": ["Docker & Kubernetes", "AWS & GCP", "CI/CD Pipelines", "Terraform"]
}

PROJECTS = [
    {
        "title": "Usando Python",
        "url": "https://github.com/PaulodiasDeveloper/Curso_EBAC-Profissao_Cientista_de_Dados",
        "description": "Projetos do curso ciêntista de dados."
    },
    
    {
        "title": "Usando Python",
        "url": "https://github.com/PaulodiasDeveloper/Curso_EBAC-Profissao_Cientista_de_Dados",
        "description": "Projetos do curso ciêntista de dados."
    },
    
    {
        "title": "Usando Python",
        "url": "https://github.com/PaulodiasDeveloper/Curso_EBAC-Profissao_Cientista_de_Dados",
        "description": "Projetos do curso ciêntista de dados."
    },
    
    {
        "title": "Usando Python",
        "url": "https://github.com/PaulodiasDeveloper/Curso_EBAC-Profissao_Cientista_de_Dados",
        "description": "Projetos do curso ciêntista de dados."
    }
]


CERTIFICATIONS = [
    "Python for Data Science - EBAC",
    "Django Full Stack Developer - Udemy",
    "Machine Leerning with Python - Coursera"
]

EXPERIENCE = [
    {
        "title": "Desenvolvedor(a)",
        "company": "Empresa",
        "date": "2023 - Presente",
        "description": ""
    },
    
    {
        "title": "Desenvolvedor(a)",
        "company": "Empresa",
        "date": "2023 - Presente",
        "description": ""
    },
    
    {
        "title": "Desenvolvedor(a)",
        "company": "Empresa",
        "date": "2023 - Presente",
        "description": ""
    }
]

def load_css():
        """Carrega todos os estilos CSS"""
        st.markdown("""
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
            <style>
                :root {
                    --primary-color: #1a365d;
                    --secondary-color: #2d547d;
                    --accent-color: #38bdf8;
                    --text-light: #f8fafc;
                    --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                }


                .project-card {
                    background: white;
                    border-radius: 10px;
                    padding: 1.5rem;
                    margin-bottom: 1.5rem;
                    box-shadow: var(--shadow);
                    transition: all 0.3s ease;
                    border: 1px solid rgba(0, 0, 0, 0.1);
                }


                .project-card:hover {
                    transform: translateY(-5px);
                    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
                }


                .experience-item {
                    padding: 1.5rem;
                    background: white;
                    border-radius: 10px;
                    box-shadow: var(--shadow);
                    margin-bottom: 1.5rem;
                    transition: all 0.3s ease;
                }


                .experience-item:hover {
                    transform: translateY(-3px);
                }
                
            </style>
        """, unsafe_allow_html=True)
        

# Redes Sociais
def social_links():
    links_html = "".join(
        f'<a href={info["url"]} target="_blank" style="margin: 0 10px; font-size: 1.5rem; color: var(--primary-color);">'
        f'<i class="{info["icon"]}"></i></a>'
        for name, info in SOCIAL_LINKS.items()
    )
    st.markdown(f'<div style="text-align: center; margin: 2rem 0;">{links_html}</div>', unsafe_allow_html=True)


# Projetos
def show_projects():
    st.markdown("## 🏗️ Projetos Recentes")
    cols = st.columns(3)
    for idx, project in enumerate(PROJECTS):
        with cols[idx % 3]:
            st.markdown(f"""
                <div class="project-card">
                    <h3><a href="{project['url']}" target="_blank">{project['title']}</a></h3>
                    <p>{project['description']}</p>
                </div>   
            """, unsafe_allow_html=True)


def show_experience():
    st.markdown("## 💼 Experiência Profissional")
    cols = st.columns(3)
    for exp in EXPERIENCE:
            st.markdown(f"""
                <div class="experience-item">
                    <h3>{exp['title']}</h3>
                    <p><strong>{exp['company']}</strong></p>
                    <p>{exp['description']}</p>
                </div>   
            """, unsafe_allow_html=True)


# 🚀 6. Código principal
def main():
    load_css() # Rodar o css
    
    
    # Sidebar
    with st.sidebar:
        
            st.image("img/profile_image.png", use_container_width=True)

        
            st.markdown("""
                <div style="text-align: center;">
                    <h2>Paulo Roberto</h2>
                    <p style="color: var(--accent-color);">💻 Software Engineer</p>
                </div>
            """, unsafe_allow_html=True)
            
            # Contato
            with st.expander("📫 Contato", expanded=True):
                    st.markdown("""
                  <p><i class="fas fa-map-marker-alt"></i> Macaé, Rio de Janeiro</p>      
                  <p><i class="fas fa-phone"></i> 22 9 9872-4205</p>      
                  <p><i class="fas fa-envelope"></i> paulodiastst@gmail.com</p>              
            """, unsafe_allow_html=True)
                    
            social_links()
            
    # Conteudo Principal
    st.title("Paulo Roberto")
    st.markdown("### Software Engineer | Data Scientist | SQL | Python | DAX | VBA | Power Bi | PHP")
    
    # Sobre mim
    with st.container():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("""
                        ## 💻 Sobre Mim
                        Olá 👋, meu nome é Paulo! Sou apaixonado por desenvolvimento de software e Data Science, sempre motivado a explorar novas tecnologias e enfrentar desafios complexos.

                        🎓 Tenho formação em Data Science pela EBAC e em Engenharia de Software pela UNOPAR.

                        🚀 Estou em busca de oportunidade profissional na área de TI, com o objetivo de atuar como desenvolvedor ou cientista de dados. Estou pronto para contribuir, aprender e crescer junto com uma equipe comprometida com inovação e resultados.
                        """, unsafe_allow_html=True)
            
        with col2:
            st.image(r"C:\Users\Paulo Roberto\Downloads\portfolio_streamlit_\img\data_science.jpg", width=200)
        
    # Habilidade técnicas
    st.markdown("## 🛠️ Habilidades Técnicas")
    cols = st.columns(3)
    for idx, (title, items) in enumerate(SKILLS.items()):
        with cols[idx]:
            items_html = "".join(f"<li>{item}</li>" for item in items)
            st.markdown(f"""
                <div style="padding: 1.5rem; background: white; border-radius: 10px; box-shadow: var(--shadow);">
                    <h3>{title}</h3>
                    <ul>{items_html}</ul>
                </div>   
            """, unsafe_allow_html=True)
    
    
    # Projetos em três colunas
    show_projects()
    
    # Certificações
    st.markdown("## 📜 Certificações")
    for cert in CERTIFICATIONS:
        st.markdown(f"""
                    <div style="padding: 1rem; background: #F8FAFC; border-radius: 8px; border-left: 4px solid var(--accent-color); box-shadow: var(--shadow);">
                        📌 {cert}
                    </div>   
                """, unsafe_allow_html=True)

    # Experiencia proficional
    show_experience()

    # Rodape
    st.markdown(f"""
                    <div style="text-align: center; padding: 2rem; color: #64748b; margin-top: 4rem;">
                        © 2025 Paulo Roberto 
                    </div>   
                """, unsafe_allow_html=True)
    
        

if __name__ == "__main__":
    main()