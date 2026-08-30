<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Krishnanunni H Pillai - AI/ML Developer & Data Scientist</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --primary: #6366f1;
            --secondary: #ec4899;
            --accent: #06b6d4;
            --dark: #0f172a;
            --darker: #020617;
            --light: #f1f5f9;
            --text: #e2e8f0;
            --subtle: #64748b;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, var(--darker) 0%, #1a1f3a 100%);
            color: var(--text);
            overflow-x: hidden;
            line-height: 1.6;
        }

        /* ===== ANIMATIONS ===== */
        @keyframes typewriter {
            from { width: 0; }
            to { width: 100%; }
        }

        @keyframes blink {
            0%, 49% { border-right-color: var(--accent); }
            50%, 100% { border-right-color: transparent; }
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes slideInLeft {
            from {
                opacity: 0;
                transform: translateX(-50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @keyframes slideInRight {
            from {
                opacity: 0;
                transform: translateX(50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
        }

        @keyframes glitch {
            0% { text-shadow: -2px 0 #ec4899, 2px 0 #06b6d4; }
            20% { text-shadow: -2px 0 #06b6d4, 2px 0 #ec4899; }
            40% { text-shadow: -2px 0 #ec4899, 2px 0 #06b6d4; }
            60% { text-shadow: -2px 0 #06b6d4, 2px 0 #ec4899; }
            80% { text-shadow: -2px 0 #ec4899, 2px 0 #06b6d4; }
            100% { text-shadow: -2px 0 #06b6d4, 2px 0 #ec4899; }
        }

        @keyframes glow {
            0%, 100% { box-shadow: 0 0 20px rgba(99, 102, 241, 0.3); }
            50% { box-shadow: 0 0 40px rgba(99, 102, 241, 0.6); }
        }

        @keyframes countUp {
            from { transform: translateY(20px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }

        @keyframes shimmer {
            0% { background-position: -1000px 0; }
            100% { background-position: 1000px 0; }
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }

        /* ===== HEADER & NAVIGATION ===== */
        header {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(2, 6, 23, 0.95);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(99, 102, 241, 0.1);
            z-index: 1000;
            padding: 1.5rem 0;
        }

        .header-content {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: fadeInUp 0.8s ease;
        }

        nav {
            display: flex;
            gap: 2rem;
        }

        nav a {
            color: var(--text);
            text-decoration: none;
            transition: all 0.3s ease;
            position: relative;
            font-size: 0.95rem;
            font-weight: 500;
        }

        nav a:hover {
            color: var(--accent);
        }

        nav a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: linear-gradient(90deg, var(--accent), var(--secondary));
            transition: width 0.3s ease;
        }

        nav a:hover::after {
            width: 100%;
        }

        /* ===== HERO SECTION ===== */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: 60px;
            position: relative;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at 20% 50%, rgba(99, 102, 241, 0.1) 0%, transparent 50%);
            pointer-events: none;
        }

        .hero::after {
            content: '';
            position: absolute;
            bottom: 0;
            right: 0;
            width: 500px;
            height: 500px;
            background: radial-gradient(circle, rgba(236, 72, 153, 0.05) 0%, transparent 70%);
            pointer-events: none;
        }

        .hero-content {
            max-width: 800px;
            padding: 2rem;
            text-align: center;
            z-index: 2;
        }

        .hero-title {
            font-size: clamp(2.5rem, 8vw, 5rem);
            font-weight: 900;
            line-height: 1.1;
            margin-bottom: 1rem;
            animation: slideInLeft 1s ease;
        }

        .hero-title .highlight {
            background: linear-gradient(135deg, var(--accent) 0%, var(--secondary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .typewriter {
            font-size: 1.5rem;
            color: var(--accent);
            font-weight: 600;
            border-right: 3px solid var(--accent);
            white-space: nowrap;
            overflow: hidden;
            animation: typewriter 4s steps(50, end), blink 0.8s infinite;
            margin-bottom: 2rem;
        }

        .hero-description {
            font-size: 1.1rem;
            color: var(--subtle);
            margin-bottom: 2.5rem;
            animation: fadeInUp 1s ease 0.3s both;
            line-height: 1.8;
        }

        .cta-buttons {
            display: flex;
            gap: 1.5rem;
            justify-content: center;
            flex-wrap: wrap;
            animation: fadeInUp 1s ease 0.6s both;
        }

        .btn {
            padding: 1rem 2rem;
            border: none;
            border-radius: 8px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }

        .btn-primary {
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            color: white;
            box-shadow: 0 10px 30px rgba(99, 102, 241, 0.3);
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 20px 40px rgba(99, 102, 241, 0.5);
        }

        .btn-secondary {
            background: transparent;
            color: var(--accent);
            border: 2px solid var(--accent);
        }

        .btn-secondary:hover {
            background: rgba(6, 182, 212, 0.1);
            transform: translateY(-3px);
        }

        .scroll-indicator {
            position: absolute;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            animation: float 3s ease-in-out infinite;
            z-index: 10;
        }

        .scroll-indicator svg {
            width: 24px;
            height: 24px;
            stroke: var(--accent);
            fill: none;
            stroke-width: 2;
        }

        /* ===== ABOUT SECTION ===== */
        section {
            max-width: 1200px;
            margin: 0 auto;
            padding: 6rem 2rem;
        }

        .section-title {
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 1rem;
            display: inline-block;
        }

        .section-title::after {
            content: '';
            display: block;
            width: 80px;
            height: 4px;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
            margin-top: 0.5rem;
            border-radius: 2px;
        }

        .section-subtitle {
            color: var(--subtle);
            font-size: 1.1rem;
            margin-bottom: 3rem;
        }

        .about-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 3rem;
            align-items: center;
            margin-bottom: 3rem;
        }

        .about-text h3 {
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: var(--accent);
        }

        .about-text p {
            color: var(--subtle);
            margin-bottom: 1rem;
            line-height: 1.8;
        }

        .focus-areas {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1.5rem;
        }

        .focus-item {
            padding: 1.5rem;
            background: rgba(99, 102, 241, 0.05);
            border: 1px solid rgba(99, 102, 241, 0.1);
            border-radius: 8px;
            transition: all 0.3s ease;
            animation: fadeInUp 1s ease;
        }

        .focus-item:hover {
            background: rgba(99, 102, 241, 0.1);
            border-color: rgba(99, 102, 241, 0.3);
            transform: translateY(-5px);
        }

        .focus-item strong {
            color: var(--accent);
        }

        @media (max-width: 768px) {
            .about-grid {
                grid-template-columns: 1fr;
            }

            .focus-areas {
                grid-template-columns: 1fr;
            }
        }

        /* ===== TECH STACK ===== */
        .tech-stack {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }

        .tech-category {
            padding: 2rem;
            background: rgba(99, 102, 241, 0.05);
            border: 1px solid rgba(99, 102, 241, 0.1);
            border-radius: 12px;
            animation: fadeInUp 1s ease;
        }

        .tech-category h4 {
            color: var(--accent);
            margin-bottom: 1.5rem;
            font-size: 1.2rem;
        }

        .tech-items {
            display: flex;
            flex-wrap: wrap;
            gap: 0.75rem;
        }

        .tech-badge {
            padding: 0.5rem 1rem;
            background: rgba(6, 182, 212, 0.1);
            border: 1px solid rgba(6, 182, 212, 0.3);
            border-radius: 20px;
            font-size: 0.9rem;
            color: var(--accent);
            transition: all 0.3s ease;
            animation: fadeInUp 0.6s ease;
        }

        .tech-badge:hover {
            background: rgba(6, 182, 212, 0.2);
            transform: scale(1.05);
        }

        /* ===== SKILLS SECTION ===== */
        .skills-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }

        .skill-item {
            animation: slideInLeft 0.8s ease;
        }

        .skill-name {
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.5rem;
            font-weight: 600;
        }

        .skill-percentage {
            color: var(--accent);
            font-weight: 700;
        }

        .skill-bar {
            width: 100%;
            height: 8px;
            background: rgba(99, 102, 241, 0.1);
            border-radius: 10px;
            overflow: hidden;
            border: 1px solid rgba(99, 102, 241, 0.2);
        }

        .skill-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--primary), var(--secondary), var(--accent));
            border-radius: 10px;
            animation: slideInLeft 2s ease forwards;
            width: 0;
        }

        /* ===== PROJECTS SECTION ===== */
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }

        .project-card {
            position: relative;
            padding: 2rem;
            background: rgba(99, 102, 241, 0.05);
            border: 1px solid rgba(99, 102, 241, 0.1);
            border-radius: 12px;
            transition: all 0.3s ease;
            animation: fadeInUp 0.8s ease;
            overflow: hidden;
        }

        .project-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
            transition: left 0.5s ease;
        }

        .project-card:hover::before {
            left: 100%;
        }

        .project-card:hover {
            border-color: rgba(99, 102, 241, 0.3);
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(99, 102, 241, 0.1);
        }

        .project-header {
            display: flex;
            justify-content: space-between;
            align-items: start;
            margin-bottom: 1rem;
        }

        .project-title {
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--accent);
            margin-bottom: 0.5rem;
        }

        .project-status {
            display: inline-block;
            padding: 0.4rem 0.8rem;
            background: rgba(236, 72, 153, 0.1);
            border: 1px solid rgba(236, 72, 153, 0.3);
            border-radius: 4px;
            font-size: 0.85rem;
            color: var(--secondary);
            font-weight: 600;
        }

        .project-status.active {
            background: rgba(6, 182, 212, 0.1);
            border-color: rgba(6, 182, 212, 0.3);
            color: var(--accent);
        }

        .project-description {
            color: var(--subtle);
            margin-bottom: 1.5rem;
            line-height: 1.7;
        }

        .project-tech {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
        }

        .project-tech-badge {
            padding: 0.3rem 0.8rem;
            background: rgba(6, 182, 212, 0.1);
            border-radius: 4px;
            font-size: 0.85rem;
            color: var(--accent);
        }

        .project-link {
            color: var(--primary);
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
            display: inline-block;
        }

        .project-link:hover {
            color: var(--secondary);
            transform: translateX(5px);
        }

        /* ===== STATS SECTION ===== */
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }

        .stat-card {
            text-align: center;
            padding: 2rem;
            background: rgba(99, 102, 241, 0.05);
            border: 1px solid rgba(99, 102, 241, 0.1);
            border-radius: 12px;
            animation: fadeInUp 0.8s ease;
        }

        .stat-number {
            font-size: 3rem;
            font-weight: 900;
            background: linear-gradient(135deg, var(--accent) 0%, var(--secondary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: countUp 2s ease forwards;
        }

        .stat-label {
            color: var(--subtle);
            margin-top: 0.5rem;
            font-weight: 600;
        }

        /* ===== ACHIEVEMENTS ===== */
        .achievement-timeline {
            display: grid;
            gap: 1.5rem;
            margin-top: 2rem;
        }

        .achievement-item {
            padding: 1.5rem;
            background: rgba(99, 102, 241, 0.05);
            border-left: 4px solid var(--primary);
            border-radius: 8px;
            animation: slideInLeft 0.8s ease;
        }

        .achievement-item:hover {
            background: rgba(99, 102, 241, 0.1);
            border-left-color: var(--secondary);
        }

        .achievement-year {
            color: var(--accent);
            font-weight: 700;
            font-size: 0.9rem;
        }

        .achievement-title {
            font-size: 1.1rem;
            font-weight: 700;
            margin-top: 0.3rem;
        }

        /* ===== CONTACT SECTION ===== */
        .contact-section {
            text-align: center;
            padding: 4rem 2rem;
        }

        .contact-section .section-title {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            display: block;
            text-align: center;
        }

        .contact-description {
            color: var(--subtle);
            font-size: 1.1rem;
            margin-bottom: 2.5rem;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }

        .social-links {
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            flex-wrap: wrap;
            margin-bottom: 2rem;
        }

        .social-link {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 60px;
            height: 60px;
            border: 2px solid rgba(99, 102, 241, 0.3);
            border-radius: 50%;
            color: var(--accent);
            text-decoration: none;
            transition: all 0.3s ease;
            font-size: 1.5rem;
        }

        .social-link:hover {
            border-color: var(--accent);
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(99, 102, 241, 0.2);
        }

        /* ===== FOOTER ===== */
        footer {
            text-align: center;
            padding: 2rem;
            background: rgba(2, 6, 23, 0.5);
            border-top: 1px solid rgba(99, 102, 241, 0.1);
            color: var(--subtle);
            font-size: 0.9rem;
        }

        /* ===== RESPONSIVENESS ===== */
        @media (max-width: 768px) {
            nav {
                display: none;
            }

            .hero {
                margin-top: 80px;
            }

            section {
                padding: 4rem 1.5rem;
            }

            .section-title {
                font-size: 2rem;
            }

            .projects-grid {
                grid-template-columns: 1fr;
            }

            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
    </style>
</head>
<body>
    <!-- HEADER -->
    <header>
        <div class="header-content">
            <div class="logo">K.H.P</div>
            <nav>
                <a href="#about">About</a>
                <a href="#skills">Skills</a>
                <a href="#projects">Projects</a>
                <a href="#contact">Contact</a>
            </nav>
        </div>
    </header>

    <!-- HERO SECTION -->
    <section class="hero">
        <div class="hero-content">
            <h1 class="hero-title">
                Hey, I'm <span class="highlight">Krishnanunni</span>
            </h1>
            <p class="typewriter">Building intelligent systems & scalable applications</p>
            <p class="hero-description">
                Computer Science Engineer | Data Scientist | Full-Stack Developer | AI/ML Enthusiast
                <br><br>
                I transform ideas into reality through code, data, and innovation.
            </p>
            <div class="cta-buttons">
                <a href="#projects" class="btn btn-primary">View My Work</a>
                <a href="mailto:krishnanunni.official.dev@gmail.com" class="btn btn-secondary">Get In Touch</a>
            </div>
        </div>
        <div class="scroll-indicator">
            <svg viewBox="0 0 24 24">
                <path d="M7 10l5 5 5-5z"></path>
            </svg>
        </div>
    </section>

    <!-- ABOUT SECTION -->
    <section id="about">
        <h2 class="section-title">About Me</h2>
        <p class="section-subtitle">Passionate about building solutions at the intersection of AI, data, and engineering</p>
        
        <div class="about-grid">
            <div class="about-text">
                <h3>What I Do</h3>
                <p>
                    I'm a Computer Science Engineering student specializing in Data Science. I love building AI-powered applications, 
                    scalable systems, and solving real-world problems with technology.
                </p>
                <p>
                    My focus spans full-stack development, machine learning, data science, and cloud architecture. 
                    I'm passionate about turning complex problems into elegant solutions.
                </p>
            </div>
            <div class="focus-areas">
                <div class="focus-item">
                    <strong>🤖 AI & Machine Learning</strong>
                    <p>Deep learning, NLP, computer vision, and intelligent systems</p>
                </div>
                <div class="focus-item">
                    <strong>🌐 Full-Stack Development</strong>
                    <p>React, Node.js, Next.js, and scalable backend architectures</p>
                </div>
                <div class="focus-item">
                    <strong>📊 Data Science</strong>
                    <p>Analytics, predictive modeling, and data visualization</p>
                </div>
                <div class="focus-item">
                    <strong>☁️ Cloud & DevOps</strong>
                    <p>GCP, Firebase, Docker, and modern deployment strategies</p>
                </div>
            </div>
        </div>
    </section>

    <!-- TECH STACK -->
    <section>
        <h2 class="section-title">Tech Stack</h2>
        <p class="section-subtitle">Tools and technologies I work with</p>
        
        <div class="tech-stack">
            <div class="tech-category">
                <h4>Languages</h4>
                <div class="tech-items">
                    <span class="tech-badge">Python</span>
                    <span class="tech-badge">JavaScript</span>
                    <span class="tech-badge">TypeScript</span>
                    <span class="tech-badge">Java</span>
                    <span class="tech-badge">C++</span>
                </div>
            </div>
            <div class="tech-category">
                <h4>Web & Backend</h4>
                <div class="tech-items">
                    <span class="tech-badge">React</span>
                    <span class="tech-badge">Next.js</span>
                    <span class="tech-badge">Node.js</span>
                    <span class="tech-badge">Express</span>
                    <span class="tech-badge">Fastify</span>
                    <span class="tech-badge">PostgreSQL</span>
                </div>
            </div>
            <div class="tech-category">
                <h4>AI/ML</h4>
                <div class="tech-items">
                    <span class="tech-badge">PyTorch</span>
                    <span class="tech-badge">TensorFlow</span>
                    <span class="tech-badge">Scikit-learn</span>
                    <span class="tech-badge">Pandas</span>
                    <span class="tech-badge">HuggingFace</span>
                </div>
            </div>
            <div class="tech-category">
                <h4>Tools & Cloud</h4>
                <div class="tech-items">
                    <span class="tech-badge">GCP</span>
                    <span class="tech-badge">Firebase</span>
                    <span class="tech-badge">Docker</span>
                    <span class="tech-badge">Git</span>
                    <span class="tech-badge">Linux</span>
                </div>
            </div>
        </div>
    </section>

    <!-- SKILLS WITH BARS -->
    <section id="skills">
        <h2 class="section-title">Skills</h2>
        <p class="section-subtitle">Proficiency in key areas</p>
        
        <div class="skills-container">
            <div class="skill-item">
                <div class="skill-name">
                    <span>Python & ML</span>
                    <span class="skill-percentage">95%</span>
                </div>
                <div class="skill-bar">
                    <div class="skill-fill" style="width: 95%; animation-delay: 0s;"></div>
                </div>
            </div>
            <div class="skill-item">
                <div class="skill-name">
                    <span>Full-Stack Development</span>
                    <span class="skill-percentage">90%</span>
                </div>
                <div class="skill-bar">
                    <div class="skill-fill" style="width: 90%; animation-delay: 0.1s;"></div>
                </div>
            </div>
            <div class="skill-item">
                <div class="skill-name">
                    <span>Data Science & Analytics</span>
                    <span class="skill-percentage">88%</span>
                </div>
                <div class="skill-bar">
                    <div class="skill-fill" style="width: 88%; animation-delay: 0.2s;"></div>
                </div>
            </div>
            <div class="skill-item">
                <div class="skill-name">
                    <span>Cloud Architecture</span>
                    <span class="skill-percentage">85%</span>
                </div>
                <div class="skill-bar">
                    <div class="skill-fill" style="width: 85%; animation-delay: 0.3s;"></div>
                </div>
            </div>
            <div class="skill-item">
                <div class="skill-name">
                    <span>System Design</span>
                    <span class="skill-percentage">82%</span>
                </div>
                <div class="skill-bar">
                    <div class="skill-fill" style="width: 82%; animation-delay: 0.4s;"></div>
                </div>
            </div>
            <div class="skill-item">
                <div class="skill-name">
                    <span>DevOps & Docker</span>
                    <span class="skill-percentage">80%</span>
                </div>
                <div class="skill-bar">
                    <div class="skill-fill" style="width: 80%; animation-delay: 0.5s;"></div>
                </div>
            </div>
        </div>
    </section>

    <!-- PROJECTS SECTION -->
    <section id="projects">
        <h2 class="section-title">Featured Projects</h2>
        <p class="section-subtitle">Real-world solutions I've built</p>
        
        <div class="projects-grid">
            <div class="project-card">
                <div class="project-header">
                    <div>
                        <h3 class="project-title">🎧 UAPR</h3>
                    </div>
                    <span class="project-status active">Active</span>
                </div>
                <p class="project-description">
                    Universal Audio Priority Ranker - AI-powered audio analysis system that detects sounds and determines priority.
                </p>
                <div class="project-tech">
                    <span class="project-tech-badge">Python</span>
                    <span class="project-tech-badge">PyTorch</span>
                    <span class="project-tech-badge">YAMNet</span>
                </div>
                <a href="https://github.com/krishnanunni6707/UAPR" class="project-link">View Project →</a>
            </div>

            <div class="project-card">
                <div class="project-header">
                    <div>
                        <h3 class="project-title">🏗️ PRAYAG</h3>
                    </div>
                    <span class="project-status active">In Dev</span>
                </div>
                <p class="project-description">
                    Event management backend using Fastify + TypeScript. Handles authentication, QR check-ins, and registrations.
                </p>
                <div class="project-tech">
                    <span class="project-tech-badge">Fastify</span>
                    <span class="project-tech-badge">TypeScript</span>
                    <span class="project-tech-badge">Supabase</span>
                </div>
                <a href="https://github.com/krishnanunni6707" class="project-link">View Project →</a>
            </div>

            <div class="project-card">
                <div class="project-header">
                    <div>
                        <h3 class="project-title">🏛️ gen-gov</h3>
                    </div>
                    <span class="project-status">Research</span>
                </div>
                <p class="project-description">
                    Government schemes RAG platform combining FastAPI + Next.js with ChromaDB and LLMs for intelligent retrieval.
                </p>
                <div class="project-tech">
                    <span class="project-tech-badge">FastAPI</span>
                    <span class="project-tech-badge">Next.js</span>
                    <span class="project-tech-badge">ChromaDB</span>
                </div>
                <a href="https://github.com/krishnanunni6707" class="project-link">View Project →</a>
            </div>

            <div class="project-card">
                <div class="project-header">
                    <div>
                        <h3 class="project-title">🚁 Drone GCS</h3>
                    </div>
                    <span class="project-status active">Production</span>
                </div>
                <p class="project-description">
                    Agricultural drone ground control system with mission planning, telemetry monitoring, and precision spraying.
                </p>
                <div class="project-tech">
                    <span class="project-tech-badge">Android</span>
                    <span class="project-tech-badge">MAVLink</span>
                    <span class="project-tech-badge">PX4</span>
                </div>
                <a href="https://github.com/krishnanunni6707" class="project-link">View Project →</a>
            </div>

            <div class="project-card">
                <div class="project-header">
                    <div>
                        <h3 class="project-title">🖨️ Smart Printing</h3>
                    </div>
                    <span class="project-status active">Active</span>
                </div>
                <p class="project-description">
                    Campus printing platform reducing queues. Digital job submission, real-time tracking, and admin analytics.
                </p>
                <div class="project-tech">
                    <span class="project-tech-badge">React</span>
                    <span class="project-tech-badge">Node.js</span>
                    <span class="project-tech-badge">Firebase</span>
                </div>
                <a href="https://github.com/krishnanunni6707" class="project-link">View Project →</a>
            </div>

            <div class="project-card">
                <div class="project-header">
                    <div>
                        <h3 class="project-title">📝 NLP Pipeline</h3>
                    </div>
                    <span class="project-status">Research</span>
                </div>
                <p class="project-description">
                    Dual-path Hindi/English NLP with sentiment analysis and emotion-aware summarization using IndicBERT.
                </p>
                <div class="project-tech">
                    <span class="project-tech-badge">PyTorch</span>
                    <span class="project-tech-badge">IndicBERT</span>
                    <span class="project-tech-badge">NLP</span>
                </div>
                <a href="https://github.com/krishnanunni6707" class="project-link">View Project →</a>
            </div>
        </div>
    </section>

    <!-- STATS SECTION -->
    <section>
        <h2 class="section-title">By The Numbers</h2>
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-number" data-target="11">0</div>
                <p class="stat-label">Active Projects</p>
            </div>
            <div class="stat-card">
                <div class="stat-number" data-target="50">0</div>
                <p class="stat-label">GitHub Contributions</p>
            </div>
            <div class="stat-card">
                <div class="stat-number" data-target="8">0</div>
                <p class="stat-label">Languages</p>
            </div>
            <div class="stat-card">
                <div class="stat-number" data-target="2">0</div>
                <p class="stat-label">Years Experience</p>
            </div>
        </div>
    </section>

    <!-- ACHIEVEMENTS -->
    <section>
        <h2 class="section-title">Achievements</h2>
        <div class="achievement-timeline">
            <div class="achievement-item">
                <div class="achievement-year">🏆 2025</div>
                <div class="achievement-title">Top 6 — HackQuest'25 National Hackathon</div>
            </div>
            <div class="achievement-item">
                <div class="achievement-year">📄 2025</div>
                <div class="achievement-title">Research Presentation — CISCom 2025</div>
            </div>
            <div class="achievement-item">
                <div class="achievement-year">🥇 2024</div>
                <div class="achievement-title">Best Idea — Code for College</div>
            </div>
            <div class="achievement-item">
                <div class="achievement-year">🎤 2024</div>
                <div class="achievement-title">Active Community Mentor & Technical Lead</div>
            </div>
        </div>
    </section>

    <!-- CONTACT SECTION -->
    <section id="contact" class="contact-section">
        <h2 class="section-title">Let's Connect</h2>
        <p class="contact-description">
            I'm always interested in new opportunities, collaborations, and interesting technical challenges. 
            Feel free to reach out!
        </p>
        <div class="social-links">
            <a href="https://github.com/krishnanunni6707" class="social-link" title="GitHub">
                <span>💻</span>
            </a>
            <a href="https://www.linkedin.com/in/krishnanunni-h-pillai-b87448327" class="social-link" title="LinkedIn">
                <span>💼</span>
            </a>
            <a href="mailto:krishnanunni.official.dev@gmail.com" class="social-link" title="Email">
                <span>📧</span>
            </a>
        </div>
        <a href="mailto:krishnanunni.official.dev@gmail.com" class="btn btn-primary">Send Me An Email</a>
    </section>

    <!-- FOOTER -->
    <footer>
        <p>© 2025 Krishnanunni H Pillai. All rights reserved. | Built with passion & code</p>
        <p>
            <span style="color: var(--accent);">❤️</span> 
            "Build. Break. Learn. Repeat."
        </p>
    </footer>

    <script>
        // Animate counter numbers
        const animateCounters = () => {
            const statNumbers = document.querySelectorAll('.stat-number');
            
            statNumbers.forEach(stat => {
                const target = parseInt(stat.getAttribute('data-target'));
                const increment = target / 50;
                let current = 0;
                
                const interval = setInterval(() => {
                    current += increment;
                    if (current >= target) {
                        stat.textContent = target;
                        clearInterval(interval);
                    } else {
                        stat.textContent = Math.floor(current);
                    }
                }, 30);
            });
        };

        // Intersection Observer for animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.animation = entry.target.dataset.animation || 'fadeInUp 0.8s ease forwards';
                    if (entry.target.classList.contains('stat-number')) {
                        animateCounters();
                    }
                }
            });
        }, observerOptions);

        // Observe all animated elements
        document.querySelectorAll('[data-animation]').forEach(el => {
            observer.observe(el);
        });

        // Smooth scroll for navigation
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            });
        });

        // Add scroll animation for projects
        window.addEventListener('scroll', () => {
            const cards = document.querySelectorAll('.project-card');
            cards.forEach(card => {
                const rect = card.getBoundingClientRect();
                if (rect.top < window.innerHeight - 50) {
                    card.style.opacity = '1';
                    card.style.transform = 'translateY(0)';
                }
            });
        });

        // Initialize
        document.addEventListener('DOMContentLoaded', () => {
            animateCounters();
        });
    </script>
</body>
</html>
