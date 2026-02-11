#!/usr/bin/env python3
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = '''<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Создать</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    <style>
        :root {
            --primary: #000000;
            --secondary: #c0c0c0;
            --accent: #ffffff;
        }
        
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: 'Arial', 'Helvetica', sans-serif;
            overflow-x: hidden;
        }
        
        .navbar {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            padding: 1rem 0;
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
        }
        
        .navbar-brand {
            font-size: 1.8rem;
            font-weight: 800;
            color: white !important;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        
        .nav-link {
            color: rgba(255,255,255,0.9) !important;
            font-weight: 600;
            margin: 0 1rem;
            transition: all 0.3s;
        }
        
        .nav-link:hover {
            color: white !important;
            transform: translateY(-2px);
        }
        
        .hero {
            min-height: 100vh;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            color: white;
            margin-top: 70px;
            position: relative;
            overflow: hidden;
        }
        
        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
            animation: pulse 10s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }
        
        .hero-content {
            position: relative;
            z-index: 1;
            max-width: 900px;
            padding: 2rem;
        }
        
        .hero h1 {
            font-size: 4rem;
            font-weight: 900;
            margin-bottom: 1.5rem;
            text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
            animation: fadeInUp 1s;
        }
        
        .hero p {
            font-size: 1.3rem;
            margin-bottom: 2rem;
            line-height: 1.8;
        }
        
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(50px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .btn-hero {
            background: white;
            color: var(--primary);
            border: none;
            padding: 18px 50px;
            font-size: 1.2rem;
            font-weight: 700;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.4s;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            text-transform: uppercase;
        }
        
        .btn-hero:hover {
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 15px 40px rgba(0,0,0,0.4);
        }
        
        section { padding: 100px 0; }
        
        .section-title {
            text-align: center;
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 4rem;
            color: var(--primary);
        }
        
        .section-title::after {
            content: '';
            display: block;
            width: 100px;
            height: 4px;
            background: var(--secondary);
            margin: 1rem auto 0;
        }
        
        .feature-card {
            background: white;
            border-radius: 20px;
            padding: 3rem 2rem;
            text-align: center;
            box-shadow: 0 10px 40px rgba(0,0,0,0.08);
            transition: all 0.4s;
            height: 100%;
        }
        
        .feature-card:hover {
            transform: translateY(-15px);
            box-shadow: 0 20px 60px rgba(0,0,0,0.15);
        }
        
        .feature-icon {
            font-size: 4rem;
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1.5rem;
        }
        
        .feature-card h3 {
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 1rem;
            color: var(--primary);
        }
        
        .product-card {
            background: white;
            border-radius: 15px;
            overflow: hidden;
            box-shadow: 0 8px 30px rgba(0,0,0,0.1);
            transition: all 0.4s;
            height: 100%;
        }
        
        .product-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 50px rgba(0,0,0,0.2);
        }
        
        .product-img {
            width: 100%;
            height: 250px;
            background: linear-gradient(135deg, #f5f5f5, #e0e0e0);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 4rem;
            color: var(--secondary);
        }
        
        .product-body {
            padding: 2rem;
        }
        
        .product-title {
            font-size: 1.4rem;
            font-weight: 700;
            margin-bottom: 0.8rem;
        }
        
        .product-price {
            font-size: 1.8rem;
            font-weight: 800;
            color: var(--secondary);
            margin-bottom: 1rem;
        }
        
        .btn-product {
            background: var(--primary);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 25px;
            font-weight: 600;
            width: 100%;
            transition: all 0.3s;
        }
        
        .btn-product:hover {
            background: var(--secondary);
            transform: scale(1.05);
        }
        
        .search-box {
            max-width: 700px;
            margin: 0 auto 4rem;
            position: relative;
        }
        
        .search-box input {
            width: 100%;
            padding: 20px 60px 20px 25px;
            border: 3px solid var(--secondary);
            border-radius: 50px;
            font-size: 1.1rem;
        }
        
        .search-box button {
            position: absolute;
            right: 5px;
            top: 50%;
            transform: translateY(-50%);
            background: var(--primary);
            color: white;
            border: none;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            cursor: pointer;
        }
        
        .contact-form {
            background: white;
            padding: 3rem;
            border-radius: 20px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }
        
        .form-control {
            padding: 15px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            margin-bottom: 1.5rem;
        }
        
        .btn-submit {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            border: none;
            padding: 15px 40px;
            border-radius: 50px;
            font-weight: 700;
            width: 100%;
        }
        
        footer {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            padding: 4rem 0 2rem;
            text-align: center;
        }
        
        @media (max-width: 768px) {
            .hero h1 { font-size: 2.5rem; }
            .section-title { font-size: 2rem; }
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg">
        <div class="container">
            <a class="navbar-brand" href="#">Создать</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#nav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="nav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link" href="#home">Главная</a></li>
                    <li class="nav-item"><a class="nav-link" href="#catalog">Каталог</a></li>
                    <li class="nav-item"><a class="nav-link" href="#services">Услуги</a></li>
                    <li class="nav-item"><a class="nav-link" href="#about">О нас</a></li>
                    <li class="nav-item"><a class="nav-link" href="#contact">Контакты</a></li>
                </ul>
            </div>
        </div>
    </nav>

    <section id="home" class="hero">
        <div class="hero-content">
            <h1 data-aos="fade-up">Создать</h1>
            <p data-aos="fade-up" data-aos-delay="200">
                Широкий ассортимент оригинальных товаров. Официальный дилер с гарантией качества.
            </p>
            <button class="btn-hero" data-aos="fade-up" data-aos-delay="400">
                <i class="fas fa-rocket me-2"></i>Начать
            </button>
        </div>
    </section>

    <section style="padding: 50px 0; background: #f8f9fa;">
        <div class="container">
            <div class="search-box">
                <input type="text" placeholder="Поиск по каталогу...">
                <button><i class="fas fa-search"></i></button>
            </div>
        </div>
    </section>

    <section id="catalog">
        <div class="container">
            <h2 class="section-title" data-aos="fade-up">Каталог товаров</h2>
            <div class="row g-4">
                <div class="col-md-4" data-aos="fade-up">
                    <div class="product-card">
                        <div class="product-img"><i class="fas fa-cog"></i></div>
                        <div class="product-body">
                            <h3 class="product-title">Запчасть A-класс</h3>
                            <p class="product-price">25 000 ₽</p>
                            <button class="btn-product"><i class="fas fa-cart-plus me-2"></i>В корзину</button>
                        </div>
                    </div>
                </div>
                <div class="col-md-4" data-aos="fade-up" data-aos-delay="100">
                    <div class="product-card">
                        <div class="product-img"><i class="fas fa-tools"></i></div>
                        <div class="product-body">
                            <h3 class="product-title">Запчасть C-класс</h3>
                            <p class="product-price">35 000 ₽</p>
                            <button class="btn-product"><i class="fas fa-cart-plus me-2"></i>В корзину</button>
                        </div>
                    </div>
                </div>
                <div class="col-md-4" data-aos="fade-up" data-aos-delay="200">
                    <div class="product-card">
                        <div class="product-img"><i class="fas fa-car"></i></div>
                        <div class="product-body">
                            <h3 class="product-title">Запчасть E-класс</h3>
                            <p class="product-price">45 000 ₽</p>
                            <button class="btn-product"><i class="fas fa-cart-plus me-2"></i>В корзину</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="services" style="background: #f8f9fa;">
        <div class="container">
            <h2 class="section-title" data-aos="fade-up">Наши услуги</h2>
            <div class="row g-4">
                <div class="col-md-4" data-aos="fade-up">
                    <div class="feature-card">
                        <i class="fas fa-wrench feature-icon"></i>
                        <h3>Установка</h3>
                        <p>Профессиональная установка с гарантией</p>
                    </div>
                </div>
                <div class="col-md-4" data-aos="fade-up" data-aos-delay="100">
                    <div class="feature-card">
                        <i class="fas fa-stethoscope feature-icon"></i>
                        <h3>Диагностика</h3>
                        <p>Полная диагностика на современном оборудовании</p>
                    </div>
                </div>
                <div class="col-md-4" data-aos="fade-up" data-aos-delay="200">
                    <div class="feature-card">
                        <i class="fas fa-cogs feature-icon"></i>
                        <h3>Ремонт</h3>
                        <p>Качественный ремонт любой сложности</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="about">
        <div class="container">
            <h2 class="section-title" data-aos="fade-up">О компании</h2>
            <div class="row align-items-center">
                <div class="col-md-6" data-aos="fade-right">
                    <h3 style="font-size: 2rem; font-weight: 700; margin-bottom: 1.5rem;">Официальный дилер</h3>
                    <p style="font-size: 1.1rem; line-height: 1.8; color: #666;">
                        Мы являемся официальным дилером с многолетним опытом. Гарантируем только оригинальные товары и профессиональное обслуживание.
                    </p>
                </div>
                <div class="col-md-6" data-aos="fade-left">
                    <div class="feature-card">
                        <i class="fas fa-award feature-icon" style="font-size: 5rem;"></i>
                        <h3>Гарантия качества</h3>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="contact" style="background: #f8f9fa;">
        <div class="container">
            <h2 class="section-title" data-aos="fade-up">Контакты</h2>
            <div class="row justify-content-center">
                <div class="col-md-8" data-aos="fade-up">
                    <div class="contact-form">
                        <form>
                            <input type="text" class="form-control" placeholder="Ваше имя">
                            <input type="email" class="form-control" placeholder="Email">
                            <input type="tel" class="form-control" placeholder="Телефон">
                            <textarea class="form-control" rows="5" placeholder="Сообщение"></textarea>
                            <button type="submit" class="btn-submit">
                                <i class="fas fa-paper-plane me-2"></i>Отправить
                            </button>
                        </form>
                    </div>
                </div>
            </div>
            <div class="row mt-5 text-center">
                <div class="col-md-4" data-aos="fade-up">
                    <i class="fas fa-map-marker-alt" style="font-size: 3rem; color: var(--primary); margin-bottom: 1rem;"></i>
                    <h4>Адрес</h4>
                    <p>г. Москва, ул. Примерная, 1</p>
                </div>
                <div class="col-md-4" data-aos="fade-up" data-aos-delay="100">
                    <i class="fas fa-phone" style="font-size: 3rem; color: var(--primary); margin-bottom: 1rem;"></i>
                    <h4>Телефон</h4>
                    <p>+7 (495) 123-45-67</p>
                </div>
                <div class="col-md-4" data-aos="fade-up" data-aos-delay="200">
                    <i class="fas fa-envelope" style="font-size: 3rem; color: var(--primary); margin-bottom: 1rem;"></i>
                    <h4>Email</h4>
                    <p>info@example.com</p>
                </div>
            </div>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2026 Создать. Все права защищены.</p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        AOS.init({duration: 1000, once: true});
        document.querySelectorAll('a[href^="#"]').forEach(a => {
            a.addEventListener('click', e => {
                e.preventDefault();
                document.querySelector(a.getAttribute('href'))?.scrollIntoView({behavior: 'smooth'});
            });
        });
    </script>
</body>
</html>'''

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=False)
