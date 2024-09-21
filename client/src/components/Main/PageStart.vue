<script>
import axios from 'axios';
import NewHeader from '../Edit/NewnavBar.vue'

export default {
    components: {
        NewHeader,
    },
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
            <div class="headernew bg-bottom">
                <!-- <NewHeader class="NewHeader" /> -->
            </div>
            <div class="greeting-text">
                <h1 class="title">Форум по <span style="color: #3b82f6;">программированию</span></h1>
                <a href="/SignUp" v-if='isL'><button class="btn-join user-select-none">Присоединиться</button></a>
                <a href="/ForumPage" v-else><button class="btn-join user-select-none">На форум</button></a>
            </div>
            <div class="description">
                <p>Здесь вы можете задать свой вопрос и вам обязательно на него ответят!</p>
            </div>
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

.navbar {
    background-color: rgba(0, 0, 0, 0.3);
    border-radius: 25px;
}

.bg-bottom {
    background-color: #3b82f6;
    opacity: 1 !important;
}

.headernew {
    display: flex;
    justify-content: center;
    width: 100%;
    margin-bottom: 0px !important;
}

.greeting-text {
    display: flex;
    flex-direction: column;
    align-items: center;
    
}

.NewHeader {
    margin-top: 20px;
    margin-bottom: 30px;
}

.greetings {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 150px;
    width: 100%;
    height: 800px;

    color: #fff;
    background-image: url(../../assets/Main/background20.png);
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: -90px -20px;
}


.description {
    margin-top: 50px;
    background-color: rgba(0, 0, 0, 0.3);
    padding: 12px 70px;
    border-radius: 20px; 
    font-size: 16px;
    font-weight: 550;
}

.description p {
    margin: 0;
}



.title {
    font-size: 40px;
    font-weight: 500;
    margin-top: 150px;
    text-shadow: 0px 1px 2px #707070;
    margin-bottom: 80px;
}

.title-desc {
    text-align: center;
    font-size: 18px;
}

.btn-join {
    width: 400px;
    height: 80px;
    font-size: 30px;
    font-weight: 500;
    border: 2px solid #fff;
    border-radius: 16px;
    background: none;
    color: #fff;
    transition: all 200ms;

}



@media (hover: hover) {
    .btn-join:hover {
        background-color: #fff;
        color: #3b82f6;
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

@media (min-width: 2100px) {
    .title {
        font-size: 60px;
    }

    .title-desc {
        font-size: 26px;
    }

    .btn-join {
        padding: 40px 85px;
        font-size: 32px;
    }
}

@media (min-width: 3400px) {
    .title {
        font-size: 80px;
    }

    .title-desc {
        font-size: 36px;
    }

    .btn-join {
        padding: 50px 100px;
        font-size: 38px;
    }

    .greetings {
        height: 800px;
    }
}

@media (min-width: 4200px) {
    .title {
        font-size: 110px;
    }

    .title-desc {
        font-size: 48px;
    }

    .btn-join {
        padding: 70px 170px;
        font-size: 55px;
    }

    .greetings {
        height: 1600px;
    }
}
</style>
