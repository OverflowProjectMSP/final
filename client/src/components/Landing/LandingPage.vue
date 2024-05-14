<script>

</script>

<template>
  <body>
    <div class="bodydiv">
      <main>
        <div class="container-second">
            <h3>
              <b>Upfollow - исследуй, общайся, делись.</b>
            </h3>
            <p>
                Присоединяйтесь к сообществу, где каждый вопрос находит ответ, а каждый ответ может стать ценным знанием для других.
            </p>
            <button type="button" class="btn">
              <span class="text"><b>Обратный отсчет</b></span>
            </button>
            <div class="deviceimg">
              <img src="../../assets/Lending/main.png" class="mainimg">
            </div>
        </div>
        <div class="h3div">
          <h3 class="best">
                <b>Преимущества</b>
          </h3>
        </div>
        <div class="container-third">
          <div class="third-mini1">
            <span class="circle">
              <img src="../../assets/Lending/search.png">
            </span>
            <h5 class="circleh5" id="search">
              <b>Поиск</b>
            </h5>
            <p class="search">
              Вы точно найдете ответ на свой вопрос
            </p>
          </div>
          <div class="third-mini2">
            <span class="circle">
              <img src="../../assets/Lending/user.png">
            </span>
            <h5 class="circleh5" id="support">
              <b>Поддержка</b>
            </h5>
            <p class="support">
              Поддержка сопроводит вас по любому вопросу
            </p>
          </div>
          <div class="third-mini3">
            <span class="circle">
              <img src="../../assets/Lendingmenu.png">
            </span>
            <h5 class="circleh5" id="interface">
              <b>Интерфейс</b>
            </h5>
            <p class="interface">
              Пользование будет приносить удовольствие
            </p>
          </div>
        </div>
        <div class="container-quadro">
          <div class="quadro-mini1">
            <h3 id="funct">
              <b>Функционал сайта</b>
            </h3>
            <p>
              Разнообразие инструментов и возможностей для эффективного обмена знаниями и опытом.
            </p>
          </div>
          <div class="quadro-mini2">
            <div class="functionimg">
              <img src="../../assets/Lending/gp.png" class="secondimg1">
            </div>
            <h5>
              <b>Задавайте свои вопросы</b>
            </h5>
            <p>
              Задавайте любые вопросы, связанные с разработкой. 
              Наши пользователи готовы помочь вам стать лучше в своей области. 
              Не стесняйтесь задавать любые вопросы и расширять свои знания.
            </p>
          </div>
          <hr>
          <div class="quadro-mini3">
            <div class="functionimg">
              <img src="../../assets/Lending/rm.png" class="secondimg2">
            </div>
            <h5>
              <b>Помогайте другим</b>
            </h5>
            <p>
              Поделитесь своими знаниями и опытом, отвечая на вопросы других участников. 
              Помогите другим стать лучше, делитесь своими идеями и решениями. 
              Ваш ответ может быть ключом к успешному развитию другого члена сообщества. 
            </p>
          </div>
        </div>
        <div class="container-five">
          <div class="bg-time">
            <h3 id="team">
              <b>Обратный отсчет</b>
            </h3>
            <h5>
              <b>23:59:59</b>
            </h5>
          </div>
        </div>
      </main>
    </div>
  </body>
  </template>
  
  <style scoped>
  /* 1. Базовые стили  */
  @import url('https://fonts.cdnfonts.com/css/rubik');
  html{
      margin: 0;
      background-color: #EEF1F4;
  }
  main{
      margin: 10px
  }
  body{
      font-family: Rubik !important;
  }
  
  /* 2. Мэйн */
  
  /* 2.1 Главная */
  
  .container-second {
    margin: 100px 120px 100px 120px;
    height: 600px;
  }
  
  .container-second h3 {
    color: #2B2D33;
    padding: 8% 0 2% 0;
    font-size: 70px;
    width: 60%;
  }
  
  .container-second p {
    font-size: 16px;
    width: 40%;
    color: #555A65;
  }
  
  .btn {
    margin-top: 2%;
    background-color: #2D72D9;
    color: #F7F8FA;
    width: 190px;
    height: 8%;
    border-radius: 10px;
  }
  
  .text {
    font-size: 16px;
  }
  
  .deviceimg {
    margin-top: -536px;
    margin-left: 1000px;
    width: 35%;
    height: 600px;
    border-radius: 10px;
  }
  
  .mainimg {
    width: 57%;
    margin-left: 120px;
  }
  
  /* 2.2 Преимущества */

  .h3div {
    margin-left: 250px;
  }
  
  .container-third {
    margin: 100px 0 100px 0;
  }
  
  .container-third h3 {
    color: #2B2D33;
    font-size: 60px;
  }
  
  .container-third p {
    color: #555A65;
  }
  
  .circle {
    display: flex;
    justify-content: center;
    padding: 12px;
    height: 50px;
    width: 50px;
    border-radius: 90px;
    background-color: #F7F8FA;
  }
  
  .container-third {
    display: flex;
    justify-content: center;
    text-align: center;
    margin-top: 100px;
    gap: 50px;
    margin-left: 50px;
  }
  
  .container-third span {
    margin-left: 130px;
    margin-bottom: 20px;
  }
  
  .container-third h5 {
    font-size: 25px;
  }
  
  .third-mini1 span {
    margin-left: 130px;
  }
  
  .third-mini2 span {
    margin-left: 160px;
  }
  
  .third-mini3 span {
    margin-left: 145px;
  }
  
  .best {
    font-size: 50px;
    margin-left: 500px;
  }
  
  /* 2.3 Функционал */
  
  .container-six {
    margin-bottom: 75px;
  }
  
  /* 2.3.1  */
  .quadro-mini1 {
    margin: 120px 80px 80px 120px;
  }
  
  .quadro-mini1 h3 {
    font-size: 50px;
    width: 30%;
    color: #2B2D33;
  }
  
  .quadro-mini1 p {
    margin-top: 30px;
    font-size: 20px;
    width: 35%;
    color: #555A65;
  }
  
  /* 2.3.2 */
  
  .quadro-mini2 {
    margin-bottom: 200px;
  }
  
  .quadro-mini2 h5 {
    margin-bottom: 25px;
    margin-left: 830px;
    margin-top: -300px;
    font-size: 40px;
  }
  
  .quadro-mini2 p {
    margin-left: 830px;
    color: #555A65;
    width: 32%;
    font-size: 20px;
  }
  
  .functionimg {
    margin-left: 5%;
    width: 45%;
    height: 500px;
    border-radius: 10px;
  }
  
  .secondimg1 {
    width: 40%;
    margin-top: -26px;
    margin-left: 150px;
  }
  
  .secondimg2 {
    width: 35%;
    margin-top: -5px;
    margin-left: 170px;
  }
  
  /* 2.3.3 */
  
  .quadro-mini3 h5 {
    margin-bottom: 25px;
    margin-left: 829px;
    margin-top: -300px;
    font-size: 40px;
  }
  
  .quadro-mini3 p {
    margin-left: 830px;
    color: #555A65;
    width: 33%;
    font-size: 20px;
  }
  
  /* 2.4 Отсчёт/переход */
  .container-five {
    margin-top: 300px;
    margin-left: 5%;
    width: 90%;
    margin-bottom: 100px;
  }
  
  .bg-time {
    border-radius: 15px;
    background-color: #F7F8FA;
    height: 250px;
  }
  
  .container-five h3 {
    padding-top: 40px;
    color: #2B2D33;
    font-size: 60px;
    text-align: center;
  }
  
  .container-five h5 {
    padding-top: 20px;
    color: #555A65;
    font-size: 60px;
    text-align: center;
  }


  @media only screen and (max-width: 320px) {

  /* Мейн */

  .deviceimg {
    width: 550px;
    margin-top: 30px;
    margin-left: -210px;
  }

  .container-second {
    margin-bottom: 950px;
  }

  .container-second h3 {
    font-size: 50px;
    margin-left: -105px;
    margin-top: -90px;
    width: 350px;
    text-align: center
  }

  .container-second p {
    width: 300px;
    font-size: 25px;
    margin-top: -5px;
    margin-left: -80px;
    text-align: center;
  }

  .container-second button {
    margin-left: -55px;
    width: 250px;
  }

  .text {
    font-size: 20px;
    text-align: center;
  }

/* Преимущества */

  .best {
    font-size: 40px;
    margin-top: -200px;
    margin-left: -220px;
    margin-bottom: -50px;
  }

  .container-third {
    display: flex;
    flex-direction: column;
    margin-left: 110px;
    width: 150px;
  }

  .container-third h5 {
    font-size: 25px;
  }

  .container-third span {
    margin-left: 50px;
  }

 /* Функционал */

 #funct {
    font-size: 40px;
    margin-left: -102px;
    margin-top: 120px;
    margin-bottom: -50px;
    display: flex;
  }
  
  .quadro-mini1 p {
    display: flex;
    text-align: left;
    width: 360px;
    margin-top: 60px;
    margin-left: -100px;
    font-size: 20px;
  }
  
  .secondimg1 {
    width: 250px;
    margin-left: -25px;
  }

  .quadro-mini2 h5 {
    margin-left: 15px;
    font-size: 35px;
    width: 350px;
    margin-top: -50px;
  }

  .quadro-mini2 p {
    margin-left: 15px;
    width: 250px;
    font-size: 20px;
  }

  hr {
    width: 430px;
    margin-top: -150px;
    margin-left: -50px;
  }

  .secondimg2 {
    width: 230px;
    margin-left: 200px;
  }

  .quadro-mini3 {
    margin-left: -100px;
  }

  .quadro-mini3 h5 {
    margin-top: -10px;
    margin-left: 240px;
    width: 200px;
    font-size: 35px;
    text-align: right;
  }

  .quadro-mini3 p {
    margin-left: 190px;
    width: 250px;
    font-size: 20px;
    display: flex;
    text-align: right;
  }
 
  /* Отсчет */

  .container-five {
    margin-left: 1px;
    width: 370px;
  }

  .container-five h3 {
    padding-top: 20px;
    padding-bottom: 20px;
    font-size: 55px;
  }

  .container-five h5 {
    padding-top: 1px;
    font-size: 60px;
  }

  .bg-time {
    height: 270px;
    margin-top: -150px;
  } 
}
@media only screen and (min-width: 321px) and (max-width: 576px) {

/* Мейн */

.deviceimg {
  width: 900px;
  margin-top: 60px;
  margin-left: -125px;
}

.container-second {
  margin-bottom: 250px;
}

.container-second h3 {
  font-size: 100px;
  margin-left: -40px;
  margin-top: -60px;
  width: 600px;
  text-align: center
}

.container-second p {
  width: 500px;
  margin-left: 5px;
  font-size: 40px;
  text-align: center;
}

.container-second button {
  margin-left: 53px;
  width: 400px;
  height: 120px;
  border-radius: 25px;
}

.text {
  font-size: 40px;
  margin-left: -5px;
}

/* Преимущества */

.best  {
  font-size: 65px;
  margin-top: 1800px;
  margin-left: -120px;
  margin-bottom: -30px;
}

.container-third {
  display: flex;
  flex-direction: column;
  margin-left: 180px;
  width: 400px;
}

.container-third h5 {
  font-size: 50px;
}

.container-third p {
  font-size: 40px;
}

.container-third span {
  margin-left: 140px;
  height: 130px;
  padding: 30px;
  width: 130px;
}

/* Функционал */

#funct {
  font-size: 65px;
  margin-left: -75px;
  margin-top: 120px;
  margin-bottom: -50px;
}

.quadro-mini1 p {
  display: flex;
  width: 500px;
  margin-top: 60px;
  margin-left: -75px;
  font-size: 40px;
}

.secondimg1 {
  width: 450px;
  margin-left: -20px;
}

.quadro-mini2 h5 {
  margin-left: 50px;
  font-size: 65px;
  text-align: left;
  width: 600px;
  margin-top: 300px;
}

.quadro-mini2 p {
  margin-left: 50px;
  text-align: left;
  width: 550px;
  font-size: 40px;
}

hr {
  width: 815px;
  margin-top: -150px;
  margin-left: -50px;
}

.secondimg2 {
  width: 385px;
  margin-left: 400px;
  margin-top: 80px;
}

.quadro-mini3 {
  margin-left: -100px;
}

.quadro-mini3 h5 {
  margin-top: 370px;
  margin-left: 420px;
  font-size: 70px;
  display: flex;
  text-align: right;
}

.quadro-mini3 p {
  margin-left: 305px;
  width: 500px;
  font-size: 30px;
  display: flex;
  text-align: right;
}

/* Отсчет */

.container-five {
  margin-left: 5px;
  width: 750px;
}

.container-five h3 {
  padding-top: 15px;
  padding-bottom: 10px;
  font-size: 85px;
}

.container-five h5 {
  padding-top: 1px;
  font-size: 80px;
}

.bg-time {
  height: 350px;
  margin-top: -250px;
}
}

@media only screen and (min-width: 577px) and (max-width: 768px) {
  /* Мейн */

  .deviceimg {
    width: 950px;
    margin-top: 30px;
    margin-left: -150px;
  }

  .container-second {
    margin-bottom: 1800px;
  }

  .container-second h3 {
    font-size: 80px;
    margin-left: 20px;
    margin-top: -90px;
    width: 450px;
    text-align: center
  }

  .container-second p {
    width: 400px;
    font-size: 35px;
    margin-top: -5px;
    margin-left: 40px;
    text-align: center;
  }

  .container-second button {
    margin-left: 65px;
    width: 350px;
    border-radius: 15px;
    height: 100px;
  }

  .text {
    font-size: 35px;
    text-align: center;
  }

/* Преимущества */

  .best {
    font-size: 60px;
    margin-top: -200px;
    margin-left: -125px;
    margin-bottom: -50px;
  }

  .container-third {
    display: flex;
    flex-direction: column;
    margin-left: 290px;
    width: 150px;
  }

  .container-third h5 {
    font-size: 25px;
  }

  .search, .support, .interface {
    font-size: 20px;
  }

  .container-third span {
    margin-left: 50px;
  }

 /* Функционал */

  #funct {
    font-size: 60px;
    margin-left: -80px;
    margin-top: 120px;
    margin-bottom: -50px;
    display: flex;
  }
  
  .quadro-mini1 p {
    display: flex;
    text-align: left;
    width: 360px;
    margin-top: 60px;
    margin-left: -80px;
    font-size: 20px;
  }
  
  .secondimg1 {
    width: 350px;
    margin-left: -30px;
  }

  .quadro-mini2 h5 {
    margin-left: 35px;
    font-size: 35px;
    width: 350px;
    margin-top: 130px;
  }

  .quadro-mini2 p {
    margin-left: 35px;
    width: 250px;
    font-size: 20px;
  }

  hr {
    width: 808px;
    margin-top: -150px;
    margin-left: -50px;
  }

  .secondimg2 {
    width: 330px;
    margin-left: 400px;
  }

  .quadro-mini3 {
    margin-left: -100px;
  }

  .quadro-mini3 h5 {
    margin-top: 200px;
    margin-left: 560px;
    width: 200px;
    font-size: 35px;
    text-align: right;
  }

  .quadro-mini3 p {
    margin-left: 510px;
    width: 250px;
    font-size: 20px;
    display: flex;
    text-align: right;
  }
 
  /* Отсчет */

  .container-five {
    margin-left: 5px;
    width: 685px;
  }

  .container-five h3 {
    padding-top: 20px;
    padding-bottom: 20px;
    font-size: 65px;
  }

  .container-five h5 {
    padding-top: 1px;
    font-size: 70px;
  }

  .bg-time {
    height: 220px;
    margin-top: -150px;
  } 
}

@media only screen and (min-width: 769px) and (max-width: 1024px) {
  /* Мейн */

  .deviceimg {
    width: 1350px;
    margin-top: 30px;
    margin-left: -120px;
  }

  .container-second {
    margin-bottom: 2500px;
  }

  .container-second h3 {
    font-size: 100px;
    margin-left: 60px;
    margin-top: -90px;
    width: 650px;
    text-align: center
  }

  .container-second p {
    width: 600px;
    font-size: 50px;
    margin-top: -5px;
    margin-left: 75px;
    text-align: center;
  }

  .container-second button {
    margin-left: 150px;
    width: 450px;
    border-radius: 18px;
    height: 120px;
  }

  .text {
    font-size: 40px;
    text-align: center;
  }

/* Преимущества */

  .best {
    font-size: 80px;
    margin-top: -200px;
    margin-left: -50px;
    margin-bottom: -50px;
  }

  .container-third {
    display: flex;
    flex-direction: column;
    margin-left: 410px;
    width: 150px;
  }

  .container-third h5 {
    font-size: 50px;
  }

  .search, .support, .interface {
    font-size: 30px;
    width: 200px;
  }

  .container-third span {
    width: 100px;
    padding: 25px;
    height: 100px;
    margin-left: 50px;
  }

  #search {
    margin-left: 20px;
  }

  #support {
    margin-left: -40px;
  }

  #interface {
    margin-left: -45px;
  }

 /* Функционал */

  #funct {
    font-size: 80px;
    margin-left: -40px;
    margin-top: 120px;
    margin-bottom: -50px;
    display: flex;
  }
  
  .quadro-mini1 p {
    display: flex;
    text-align: left;
    width: 500px;
    margin-top: 60px;
    margin-left: -40px;
    font-size: 30px;
  }
  
  .secondimg1 {
    width: 450px;
    margin-left: -20px;
  }

  .quadro-mini2 h5 {
    margin-left: 75px;
    font-size: 50px;
    width: 450px;
    margin-top: 320px;
  }

  .quadro-mini2 p {
    margin-left: 75px;
    width: 450px;
    font-size: 25px;
  }

  hr {
    width: 1063px;
    margin-top: -150px;
    margin-left: -50px;
  }

  .secondimg2 {
    width: 430px;
    margin-left: 550px;
  }

  .quadro-mini3 {
    margin-left: -100px;
  }

  .quadro-mini3 h5 {
    margin-top: 400px;
    margin-left: 720px;
    width: 300px;
    font-size: 50px;
    text-align: right;
  }

  .quadro-mini3 p {
    margin-left: 570px;
    width: 450px;
    font-size: 25px;
    display: flex;
    text-align: right;
  }
 
  /* Отсчет */

  .container-five {
    margin-left: 5px;
    width: 990px;
  }

  .container-five h3 {
    padding-top: 20px;
    padding-bottom: 20px;
    font-size: 100px;
  }

  .container-five h5 {
    padding-top: 1px;
    font-size: 110px;
  }

  .bg-time {
    height: 320px;
    margin-top: -150px;
  } 
}


</style>