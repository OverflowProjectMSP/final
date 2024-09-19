<script>

</script>

<template>
    <div class="wind">
        <button>
            <svg width="34" height="34" viewBox="0 0 34 34" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M8.4375 8.42969L25.3066 25.2988" stroke="white" stroke-width="4" stroke-linecap="round"/>
            <path d="M8.4375 25.3047L25.3066 8.43555" stroke="white" stroke-width="4" stroke-linecap="round"/>
            </svg>
        </button>
        <div class="coming-soon">
            <h1>Уже совсем скоро!!!</h1>
            <div class="uf">
                <p>UpFollow</p>
                <p>2.0</p>
            </div>
        </div>
        <div class="hello-everyone">
            <h3>Всем доброго времени суток!</h3>
            <div class="descr">
                <p>Уже более месяца мы работаем над <br> UpFollow 2.0</p>
                <p>Вас ждет крупнейшее обновление нашего форума за все время существования проекта!</p>

                <h5>Что будет доступно?</h5>
                <p>Да нихуя нового, вы увидите невъебически ахуенный редизайн <br>
                    Новый интерфейс на страницах создания вопросов и статей <br>
                    Если не будете зареганы, хуй вы что спросите и напишите <br>
                    Новый навбар и футер <br>
                    А так же крутой раздел с новостями</p>
            </div>
        </div>
        <div class="teem-hello">
            <h2>Всем привет от нашей дружной команды ;)</h2>
        </div>
    </div>
</template>

<style>

h1, h2, h3, h4, h5, p {
    color: #fff;
    margin: 0;
}



.wind {
    margin: 20px 0 20px 0;


    width: 500px;
    height: 710px;
    background-image: url(../../assets/Main/back-uftwo.png);
    background-size: cover;
    background-repeat: no-repeat;
    border-radius: 24px;

    padding: 20px 15px 20px 15px;

    display: flex;
    flex-direction: column;

    position: relative;
}

button {
    position: absolute;
    background: none;
    border: none;

    top: 15px;
    right: 15px;

}

svg path {
    transition: all 100ms;
}

button:hover svg path {
    stroke: #e4e4e4;
}

.coming-soon {
    display: flex;   
    flex-direction: column;
    align-items: center;
    gap: 40px;
}

h1 {
    font-size: 25px;
}

.uf {
    width: 320px;
    height: 120px;
    border: 2px solid #fff;
    border-radius: 24px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    margin-bottom: 50px;
}

.uf p {
    font-size: 30px;
    font-weight: 700;
}

h3 {
    font-size: 20px;
    margin-bottom: 28px;
}

.hello-everyone {
    
}

.descr {
    border-top: 2px solid #fff;
    border-bottom: 2px solid #fff;

    padding: 17px 0 10px 0;

    display: flex; 
    flex-direction: column;
    gap: 20px;
}

h5 {
    margin-top: 10px;
}


.descr p {
    font-size: 14px;
    font-weight: 500;
}

.teem-hello {
    display: flex;
    justify-content: center;

    margin: 20px;
}

h2 {
    font-size: 20px;
}

@media (max-width: 530px) {
    .wind {
        width: 450px;
        height: 750px;
    }
}

@media (max-width: 460px) {
    .wind {
        width: 350px;
        height: 800px;
    }

    h1 {
        font-size: 20px;
        margin-top: 20px;
    }

    .uf {
        width: 200px;
    }
}

</style>
