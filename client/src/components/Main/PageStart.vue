<script>
import axios from 'axios';

export default {
    data() {
        return {
            isL: true
        }
    },
    methods:{
        async isLogin(){
            let res = await axios.get('/check-r')

            if (res.data.all=='true') {
                this.isL = false; 
                return
            }
            this.isL = true;
        }
    },
    mounted(){
        this.isLogin()
    }
}
</script>

<template>
    <div class="pagestart">
        <div class="greetings">
            <h1 class="title">Форум по <span style="color: #2D72D9;">программированию</span></h1>
            <p class="title-desc">Здесь вы можете задать свой вопрос и вам обязательно <br> на него ответят!</p>
            <a href="/SignUp" v-if='isL'><button class="btn-join user-select-none">Присоединиться</button></a>
            <a href="/ForumPage" v-else><button class="btn-join user-select-none">На форум</button></a>
        </div>
    </div>
</template>

<style>
@import url('https://fonts.cdnfonts.com/css/rubik');

html,
body {
    font-family: 'rubik';
}

#app {
    font-family: 'rubik';
}

body {
    margin: 5px;
}

.greetings {
    border-radius: 0px;
    color: #fff;
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 600px;
    background-image: url(../../assets/Main/mountainsjpeg.jpeg);
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

.title {
    font-size: 40px;
    font-weight: 400;
    margin-top: 150px;
}

.title-desc {
    text-align: center;
    font-size: 18px;
}

.btn-join {
    font-weight: 600;
    background-color: #166AA7;
    color: #fff;
    box-shadow: 0px 0px 20px #166AA7;
    border: none;
    margin-top: 25px;
    padding: 30px 70px;
    border-radius: 15px;
    font-size: 24px;
    transition: all 200ms;
    cursor: pointer;
}



@media (hover: hover) {
    .btn-join:hover {
        background-color: #145482;
        box-shadow: 0px 0px 40px #145482;
        transform: scale(1.2);
    }
}

@media (min-width: 100px) and (max-width: 600px) {
    .title {
        text-align: center;
        font-size: 32px;
    }

    .title-desc {
        font-size: 16px;
    }

    .btn-join {
        padding: 20px 40px;
    }
}
</style>