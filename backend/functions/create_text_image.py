from html2image import Html2Image


def text_to_image(text: str,dir:str,name:str):
   hti = Html2Image(output_path='F:/450 project/Project/backend/'+dir,temp_path='F:/450 project/Project/backend/'+dir) 
    
   html = f'''
   <!DOCTYPE html>
   <html lang="en">

   <head>
   <meta charset="UTF-8" />
   <meta name="viewport" content="width=device-width, initial-scale=1.0" />
   <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta2/css/all.min.css" />
   <title>Hero Section Design | Hassanrao.com</title>
   </head>

   <body style='background-color: white;'>
   <header class="container">
      <nav>
         <a href="#" style="font-size: 25px;font-weight: bold;">VideoAI</a>
         
      </nav>
      <div class="hero">
         <section class="hero-left">
         <h1>{text}</h1>
         
         </section>

         <section class="right">
         <img src="https://varthana.com/school/wp-content/uploads/2022/12/B103.jpg" alt="Hero illustration" />
         </section>
      </div>
   </header>
   </body>
   </html>
   '''
   css = '''
   @import url("https://fonts.googleapis.com/css2?family=Open+Sans&family=Raleway:wght@400;700&display=swap");
   * {
   box-sizing: border-box;
   margin: 0;
   padding: 0;
   font-family: "Open Sans", sans-serif;

   }
   .container {
   width: 1500px;
   max-width: 100%;
   margin: 0 auto;
   padding: 50px 0;
   }
   a{
   text-decoration: none;
   }
   nav {
   display: flex;
   justify-content: space-between;
   }
   nav a img{
   width: 100px;
   }

   nav ul {
   display: flex;
   }

   nav li {
   list-style: none;
   margin: 0 25px;
   }
   nav ul li a {
   color: hsl(243, 87%, 12%);
   }
   nav ul li a:hover{
   text-decoration: underline;
   }
   .hero {
   display: flex;
   align-items: center;
   margin-bottom: 5rem;
   }

   .hero section {
   flex: 1;
   }
   .hero-left h1 {
   font-size: 2.5rem;
   margin-bottom: 25px;
   color: #070439;
   }

   .hero-left p {
   font-weight: 600;
   line-height: 1.5;
   margin-bottom: 25px;
   color: #444444;
   }

   .hero-left {
   padding-right: 40px;
   }
   .hero-left a {
   padding: 10px 15px;
   background: #372cfa;
   color: #fff;
   font-weight: 600;
   border-radius: 4px;
   cursor: pointer;
   border: none;
   outline: none;
   transition: 0.3s all ease;
   border-radius: 20px;
   }
   .hero-left a:hover{
   background-color: #070439;
   }
   .right {
   padding-top: 50px;
   }

   .right img {
   width: 100%;
   max-width: 100%;
   }
   @media screen and (max-width: 1000px) {
   nav img {
      width: 100px; 
   }

   nav li {
      list-style: none;
      margin: 0 8px 
   }

   .hero {
      flex-direction: column;  
      text-align: center; 
   }

   .hero .right {
      order: -1;  
      padding-bottom: 5rem; 
   }
   }'''

   # screenshot an HTML string (css is optional)
   hti.screenshot(html_str=html, css_str=css, save_as=name)