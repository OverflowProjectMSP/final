<script>
export default {
    data() {
        return {
            yes: true
        }
    },
    methods: {
        inverse() {
            this.yes = !this.yes
        }
    }
}
</script>

<template>
    <div class="head-1">
        <p class="q" @click="Olezha">Вопросы пользователя</p>
        <a class="vse" @click="inverse">Все вопросы(NaN)</a>
    </div>
</template>

<style scoped>
@import url('https://fonts.cdnfonts.com/css/rubik');

body {
    font-family: Rubik !important;
}

:root {
    --size-20: 20px;
    --size-26: 26px;
    --size-22: 22px;
    --size-18: 18px;
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
</style>