<script>
import axios from 'axios';
// import VidComp from './components/MainComponents/VidComp.vue'
import ModelWind from '../ReuseComponets/ModelWind.vue';
import VidjetComp from '../ReuseComponets/StateVid.vue';
export default {
    components: {
    // VidComp,
        ModelWind,
        VidjetComp  
    },
    data() {
        return {
            states: [],
            Show: false,
            tag: ``,

            title: ``,
            author: ``,
            cnt: 0,

            isAllLoad: false,
        }
    },
    methods: {
        OpenModal() {
            this.Show = !this.Show
        },
        CloseModal(Show) {
            this.Show = false
        },
        async loadStates() {
            let res = await axios.get('/show-states');
            this.states = res.data.all;
            this.cnt++
            // console.log(res.data)
            this.preloader();
        },

        async searchStates() {
            let res = await axios.get('/search', {
                params: {
                    title: this.title,
                    author: this.author,
                }
            });
            this.states = res.data.all;
        },

        async filtre() {
            let res = await axios.get('/filtre-states', {
                params: {
                    title: this.title,
                    author: this.author,
                    tag: this.tag,
                }
            });
            this.states = res.data.all;
        },

        async preloader() {
            if (this.states.length) {
                this.isAllLoad = true;
            }
        },
    },
    mounted() {
        this.loadStates();
    },
}
</script>

<template>

<div class="content-cont d-flex align-items-center" v-if='this.isAllLoad'>
    <!-- Компонент поиска -->
    <div class="title-text">
        <h4 class="text">Поиск статьи</h4>
    </div>
    <div class="all-inputs">
        <input v-model="title" type="search" class="form-control" placeholder="Название статьи" aria-label="First name">
        <input v-model="author" type="search" class="form-control" placeholder="Автор" aria-label="Last name">
    </div>
    <!-- селект -->
    <div class="down-menu d-flex">
        <div class="dropdown-center">
            <select class="form-select me-2" v-model="tag">
                <option value="javascript">JavaScript</option>
                <option value="ts">TS</option>
                <option value="python">Python</option>
                <option value="php">PHP</option>
                <option value="cpp">C++</option>
                <option value="java">Java</option>
                <option value="cs">C#</option>
                <option value="go">Golang</option>
                <option value="IB">ИБ</option>
                <option value="">Без фильтров</option>
            </select>
        </div>
      <!-- плюсик -->
      <!-- <div class="contain" @click="OpenModal" >
        <img src="../../assets/States/add.png" class="add" alt="">
      </div> -->
        <button class="btn find-btn btn-outline-primary  ms-4" @click="filtre">Найти</button>

        <a href="/NewState"><button class="create-state">Создать статью</button></a>
    </div>
</div>
<!-- Див с виджетами -->
<div class="conr" v-if='this.isAllLoad'>
    <div class="con" v-for="item in states">
        <a :href="`/StateItem/` + item.id">
            <!-- <vid-comp :item="item" role="button" /> -->
            <vidjet-comp :item="item"    />
        </a>
    </div>
</div>
<div class="content p-2" v-if="this.states.length == 0 && this.cnt == 1 && this.isAllLoad">
    <h2 class="d-flex justify-content-center my-5 user-select-none">Будь первым, кто даст ответ на этот вопрос!</h2>
</div>

<model-wind v-if="Show" @CloseModal="CloseModal"/>

<div class="co" v-if='!this.isAllLoad'>
    <div class="load-item item1"></div>
    <div class="load-item item2"></div>
    <div class="load-item item3"></div>
    <div class="load-item item4"></div>
    <div class="load-item item5"></div>
</div>


</template>

<style scoped>

.all-inputs {
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.content-cont {
    display: flex;
    flex-direction: column;
    gap: 5px;

    width: 100%;
}

.title-text {
    display: flex;
    justify-content: start;
    width: 800px;
}

.find-btn{
    color: black;
}
.conr{
    display: flex;
    flex-direction: column;
    align-items: center;
    overflow: scroll; 
    overflow-x: hidden;
    height: 555px;
    padding-top: 10px;
    /* width: auto;
    margin-left: auto;
    margin-right: auto; */
}
a {
    text-decoration: none;
    color: #000;
}
h4{
    /* margin-left: 20.5%;
    margin-top: 20px; */
    font-size: 40px;
    
}
.image{
    margin-right: 10px;
    width: 25px;
}
.add{
    width: 25px;
    height: 25px;
    cursor: pointer
}
.btn{
    font-size: 16px;
    font-weight: bold;
    color:rgb(0, 0, 0);

    margin: 0 !important;
}
.content {
    display: flex;
    flex-direction: column;
    gap: 5px;

    /* margin: 10px; */
    /* flex-wrap: wrap; */
    /* margin-left: 20%; */
    /* margin-bottom: 100px; */
}

.down-menu {
    width: 800px;
    display: flex;
    gap: 10px
    
}

.form-control{
    width: 800px;
}

.form-select {
    width: 320px;
    margin: 0 !important;
}

.btn {
    width: 230px;
}

.create-state {
    width: 230px;
    height: 37px;

    background-color: #3B82F6;
    color: #fff;
    border: none;
    border-radius: 5px;

    font-size: 20px;
    font-weight: 500;

    transition: all 100ms
}

.create-state:hover {
    background-color: #20498b;
}

.con{
    width: 750px;
    /* justify-content: start; */
    /* display: flex; */
}

/* .con a {
    width: 100px !important;
} */

.contain{
    width: 5%;
    height: 5%;
    
}
.plus {
    width: 30px; 
    height: 30px;
    background-color: #e8e7ea;
    border-radius: 50%; 
    border: 0.0001px solid ; 
    
    
   
}
.p{
    margin-left: 0.2px;
    margin-right: 1px;
}

@media (hover: hover) {
    .find-btn:hover{
        color: white;
        transition: all 0.5s;
    }
}

/* @media (min-width: 1900px) {
    .con {
        width: 1300px
    }
    
    .con a {
        width: 1000px !important;
    }
} */

@media (max-width: 900px){

.content input{
    width: 400px;
}

.form-select {
    width: 255px;
}

.btn {
    width: 140px;
    font-size: 14px;
    margin: 0 !important;
}

.down-menu {
    display: flex;
    justify-content: center;
}

.create {
    display: flex;
    justify-content: center;
}

.create-state {
    width: 400px;
}

.content, h4 {
    font-size: 32px;
}
.dropdown-center{
    margin: 2px !important;
}
}
@media (max-width: 900px) {
    .content, h4 {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .title-text {
        margin-left: 150px;
    }

    .form-control{
        width: 650px;
    }

    .down-menu {
        width: 650px;
    }

    h4 {
        font-size: 30px;
    }
}

@media (max-width: 650px) {
    .form-control {
        width: 450px;
    }

    .down-menu {
        width: 450px;
    }

    .title-text {
        margin-left: 350px;
    }

    .form-select {
        width: 200px;
    }

    .find-btn {
        margin-top: 3px !important;
        height: 35px;
        width: 70px;
    }

    .create-state {
        width: 200px;
        font-size: 16px;
        height: 35px;
        margin-top: 3px;
    }
}

@media (max-width: 635px) {
  .content .form-control{
    width: 400px;
   }
}

@media (max-width: 500px) {
    .down-menu {
        flex-direction: column;
        align-items: center;
        gap: 5px;
    }

    .title-text {
        margin-left: 400px;
    }

    .form-control {
        width: 400px;
    }

    .form-select {
        width: 400px;
    }

    .btn {
        width: 400px;
    }

    .create-state {
        width: 400px;
    }
}

@media (max-width: 400px) {
    .form-control {
        width: 250px !important;
    }

    .form-select {
        width: 250px;
    }

    .btn {
        width: 250px;
    }

    .create-state {
        width: 250px;
    }

    .title-text {
        margin-left: 550px;
    }
}

@media (min-width: 2100px) {
    h4 {
        font-size: 50px
    }

    .all-inputs {
        width: 1000px;
    }

    .title-text {
        width: 1000px;
    }

    .form-control {
        width: 1000px;
        height: 50px;
        font-size: 18px;
    }

    .down-menu {
        width: 1000px;
    }

    .form-select {
        width: 326px;
        height: 50px;
        font-size: 18px;
    }

    .find-btn {
        width: 326px;
        height: 50px;
        font-size: 18px;
    }

    .create-state {
        width: 326px;
        height: 50px;
        font-size: 22px;
    }

    .conr {
        height: 700px;
    }
}

@media (min-width: 3200px) {
    h4 {
        font-size: 70px
    }

    .all-inputs {
        width: 1400px;
    }

    .title-text {
        width: 1400px;
    }

    .form-control {
        border-radius: 12px;

        width: 1400px;
        height: 60px;
        font-size: 26px;
    }

    .down-menu {
        width: 1400px;
    }

    .form-select {
        border-radius: 12px !important;
        width: 460px;
        height: 60px;
        font-size: 26px;
    }

    .find-btn {
        border-radius: 12px;
        width: 460px;
        height: 60px;
        font-size: 26px;
    }

    .create-state {
        border-radius: 12px;
        width: 460px;
        height: 60px;
        font-size: 30px;
    }

    .conr {
        height: 1200px;
    }
}

@media (min-width: 4500px) {
    h4 {
        font-size: 100px
    }

    .all-inputs {
        width: 1900px;
    }

    .title-text {
        width: 1900px;
    }

    .form-control {
        border-radius: 12px;

        width: 1900px;
        height: 90px;
        font-size: 45px;
    }

    .down-menu {
        width: 1900px;
    }

    .form-select {
        border-radius: 12px !important;
        width: 627px;
        height: 90px;
        font-size: 45px;
    }

    .find-btn {
        border-radius: 12px;
        width: 627px;
        height: 90px;
        font-size: 45px;
    }

    .create-state {
        border-radius: 12px;
        width: 627px;
        height: 90px;
        font-size: 50px;
    }

    .conr {
        height: 1700px;
        gap: 30px;
    }

    .content-cont {
        margin-bottom: 60px;
    }
}


@media (min-width: 5800px) {
    h4 {
        font-size: 160px
    }

    .all-inputs {
        width: 2650px;
    }

    .title-text {
        width: 2650px;
    }

    .form-control {
        border-radius: 12px;

        width: 2650px;
        height: 120px;
        font-size: 60px;
    }

    .down-menu {
        width: 2650px;
    }

    .form-select {
        border-radius: 12px !important;
        width: 876px;
        height: 120px;
        font-size: 60px;
    }

    .find-btn {
        border-radius: 12px;
        width: 876px;
        height: 120px;
        font-size: 60px;
    }

    .create-state {
        border-radius: 12px;
        width: 876px;
        height: 120px;
        font-size: 65px;
    }

    .conr {
        height: 2400px;
        gap: 30px;
    }

    .content-cont {
        margin-bottom: 60px;
    }
}
</style>
