<script>
let elList = document.querySelectorAll(`.el`);
for (let i = 0; i < elList.length; i++) {
    let el = elList[i];
    el.classList.add(`t-alig-c`);
}
export default {
    data() {
        return {
            // item: {
            //     // title: `Как создать переменную?`,
            //     //     subscribers: 50,
            //     //     hours: 43,
            //     //     views: 43,
            //     //     answers: 423,
            //     //     language: 'Python',
            //     //     complexity: 'Средне',
            //     //     id: 0
            // },

            isCheck_class: `ch check-false`,
        }

    },
    props: {
        quetion: Object,
        Show: Boolean,
    }

}
</script>

<template>
    <a :href="`/QuestionItem?id=${quetion.id}&q=true`">
        <div class="window">
            <div class="main-container">
                <div class="cont">
                    <div class="account">
                        <!-- <img :src="'src/assets/' + avatar" alt=""> -->
                        <a href="#!"><p>{{ quetion.tag }}</p></a>
                    </div>
                    <div class="text">
                        <h5>{{ quetion.discriptions }}</h5>
                    </div>
                    <div class="info">
                        <p>{{ quetion.subscribers }} подписчиков</p>
                        <p>{{ quetion.date }}</p>
                        <p>{{ quetion.views }} просмотров</p>
                    </div>
                </div>
                <div class="ans_check">
                    <div class="d-flex flex-column check">
                        <!-- <img v-if="isCheck" width="15" src="../assets/check.svg" alt=""> -->
                        <p :class="isCheck_class">{{ quetion.answers }}</p>
                        <p :class="isCheck_class">Комментарий (-ев)</p>
                    </div>
                    <a :href="`/StateItem?id=` + quetion.id + `&question=` + quetion.question" class="answ"><button >Ответить</button></a>
                </div>
            </div>
        </div>
    </a>
</template>

<style>
.answ{
    text-align: center;
}
.window {
        display: flex;
        justify-content: center;
    }

    .main-container {
        margin: 20px;

        width: auto;
        height: auto;
        border: 1px solid #121212;
        border-radius: 15px;

        padding: 10px;

        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 50px;
    }

    @media (min-width: 1900px) {
        .main-container {
            width: 60% !important;
        }
    }

    .account {
        display: flex;
        align-items: center;
        gap: 10px;
        
    }

    .account p {
        margin: 0;
        font-size: 18px;
        font-weight: 700;
        color: #8355E3;

        font-family: "Baloo Chettan 2", sans-serif;
    }

    

    .account p:active {
        color: #51309a;
    }

    .account a {
        font-size: 12px;
        text-decoration: none;
    }

    .account img {
        width: 40px;
        border-radius: 50px;
        border: 1px solid #121212; 
    }

    .cont {
        display: flex;
        flex-direction: column;
        gap: 15px;
        /* margin-top: -45px; */
    }

    .text h5 {
        font-size: 20px;

        width: 38ch;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
    }

    .info {
        margin-top: -5px;
        display: flex;
    }
    
    .info p {
        font-size: 15px;
        color: #3B82F6;
        border-right: 1.5px solid #3B82F6;
        padding-right: 8px;
        padding-left: 8px;
    }

    .info p:last-child {
        border-right: none;
    }

    .info p:first-child {
        padding-left: 0px;
    }

    .ans_check {
        display: flex;
        flex-direction: column;
    }

    .ans_check button {
        width: 130px;
        height: auto;
        font-size: 18px;
        background-color: #3B82F6;
        border: none;
        border-radius: 8px;
        color: #fff;

        margin-bottom: 15px;
        transition: all 100ms;

        margin-top: 20px;
    }

    

    .ans_check button:active {
        background-color: #1d52a6;
    }

    .ch {
        margin: 0;
        text-align: center;
        font-size: 22px;
        font-weight: 700;
    }

    .check-false {
        color: #AEB8BC;
    }

    .check-true {
        color: #65C178;
    }

    .check {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
    }

    /* АДАПТИВКА */


    @media (hover: hover) {
        .account p:hover {
            color: #663ebc;
        }

        .ans_check button:hover {
            background-color: #2e6ac9;
        }
    }

    @media (max-width: 750px) {
        .main-container {
            flex-direction: column;
            align-items: start;
            
        }

        .ans_check button {
            width: 250px;
            margin-left: 160px;
            margin-bottom: 0;
        }

        .ans_check {
            flex-direction: row;
            align-items: center;
            gap: 10px;
            margin-top: -40px;
        }

        .check {
            margin-top: 0;
        }
    }

    @media (max-width: 540px) {
        .account img {
            width: 60px;
        }

        .account p {
            font-size: 20px;
        }

        .account a {
            font-size: 18px;
        }

        .info {
            flex-direction: column;
        }

        .info p {
            border-right: none;
            padding: 0;
            border-bottom: 2px solid #3B82F6;
            width: 150px;
            padding-bottom: 10px;
        }

        .text h5 {
            font-size: 18px;
        }

        .ans_check {
            gap: 0;
        }

        .ans_check button {
            margin-right: 30px;
        }
    }

    @media (max-width: 450px) {
        .ans_check {
            flex-direction: column;
            align-items: center;
        }

        .ans_check button {
            width: 250px;
        }

        .text h5 {
            width: 30ch;
        }
    }

    @media (max-width: 430px) {
        .account img {
            width: 40px;
        }

        .account p {
            font-size: 16px;
        }

        .account a {
            font-size: 12px;
        }

        .text h5 {
            width: 20ch;
        }

        .main-container {
            flex-direction: row;
            align-items: flex-end;
            gap: 0;
        }

        .info p {
            width: 120px;
        }

        .ans_check button {
            width: 100px;
            margin-top: 100px;
            margin-left: -30px;
        }

        .ans_check {
            align-items: flex-start;
        }

        .check {
            margin-left: 35px;
        }

        /* .ans_check button {
            width: 100px;
            font-size: 16px;
            margin-right: -20;

        } */
    }

    @media (max-width: 540px) {
        .check {
            position: absolute;
            top: 82px;
            right: 10px;
        }

        .ans_check button {
            position: absolute;
            bottom: 20px;
            right: -20px;

            width: 80px;
            font-size: 16px;

        }

        .main-container {
            position: relative;

        }
    }

    @media (max-width: 500px) {
        /* .ans_check button {
            right: 50px;
        }

        .check {
            right: 85px;
        } */

        .main-container {
            width: 400px;
        }
    }
</style>