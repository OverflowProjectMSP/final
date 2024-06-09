<script>
export default {
    data() {
        return {
            answerCount: 1,
            isCheck: false,
            isCheck_class: "ch check-false",
        }
    },
    props: {
        item: Object,
        Show: Boolean,
    }
}
</script>

<template>
    <div class="window">
        <div class="main-container">
            <div class="cont">
                <div class="account">
                    <!-- <img :src="'src/assets/' + avatar" alt=""> -->
                    <a href="#!"><p>{{ item.tag }}</p></a>
                </div>
                <div class="text">
                    <h5>{{ item.descriptions }}</h5>
                </div>
                <div class="info">
                    <p>{{ item.data }}</p>
                </div>
            </div>
            <div class="ans_check">
                <a :href="`/QuestionItem/${item.id}`"><button>Ответить</button></a>
                <div class="check">
                    <!-- <img v-if="isCheck" width="15" src="../assets/check.svg" alt=""> -->
                    <p :class="isCheck_class">{{ item.acnt }}</p>
                </div>
                <p :class="isCheck_class">Ответ</p>
            </div>
        </div>
    </div>
</template>

<style>

.main-container {
    padding-top: 10px;
    transition: all 0.5s;
}

.main-container:hover {
    transform: translateY(-10px);
    box-shadow: 10px 5px 5px rgb(0, 0, 0, 0.5);
}

.head-1 {
    margin: 0 20%;
    height: 30px;
    display: flex;
    justify-content: space-between;
    /* margin: -15px; */
    border-bottom: 1px solid #000000;
    width: 60%;
    padding-bottom: 5px;
}

.vse {
    margin: 0;
    color: #2D72D9;
    font-size: 24px;
    text-decoration: none;

}

.q {
    font-size: 24px;
    margin: 0;
}

@media(max-width: 1200px) {
    .vse {
        font-size: var(--size-20);
    }

    .q {
        font-size: var(--size-20);
    }
}

@media(max-width: 992px) {

    .vse {
        font-size: var(--size-18);
    }

    .q {
        font-size: var(--size-18);


    }
}

@media(max-width: 576px) {
    .vse {
        font-size: var(--size-18);

    }

    .q {
        font-size: var(--size-18);
    }
}

@media(max-width: 768px) {

    .vse {
        font-size: var(--size-18);
    }

    .q {
        font-size: var(--size-18);
    }

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
        gap: 50px;
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

    .account p:hover {
        color: #663ebc;
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
    }

    

    .ans_check button:active {
        background-color: #3B82F6;
        color: #fff
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
    }

    /* АДАПТИВКА */

    @media (hover: hover) {
        .ans_check button:hover {
            background-color: #2e6ac9;
        }

        .ans_check button:active {
            background-color: #1d52a6;
        }
    }

    @media (max-width: 750px) {
        .main-container {
            flex-direction: column;
            align-items: start;
            
        }

        .ans_check button {
            width: 250px;
            margin-right: 70px;
            margin-bottom: 0;
        }

        .ans_check {
            flex-direction: row;
            align-items: center;
            gap: 10px;
            margin-top: -40px;
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
</style>
