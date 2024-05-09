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
            // }
        }

    },
    props: {
        item: Object,
        Show: Boolean,
    }

}
</script>

<template>
    <div class="vid" role="button">
        <div class="left">
            <div class="top-1">
                <div class="name">
                    <p><img src="" alt="" class="t">{{ item.language }}</p>
                </div>
                <div class="id middle">
                    <p><img src="" alt="" class="t">{{ item.complexity }}</p>
                </div>
            </div>
            <div class="mid-1">
                <p class="name-limit">{{ item.title }}</p>
            </div>
            <div class="bottom-1">
                <div class="el">{{ item.subscribers }} подписчика(ов)</div>
                <div class="el">{{ item.hours }} час(ов) назад</div>
                <div class="el -d">{{ item.views }} просмотр(ов)</div>
            </div>
        </div>
        <div class="right">
            <div class="right-in">
                <p class="t-alig-c">{{ item.answers }}</p>
                <p>Ответ(ов)</p>
            </div>
        </div>
    </div>
</template>

<style>
:root {
    --size-20: 20px;
    --size-26: 26px;
    --size-22: 22px;
    --size-18: 18px;
}

.t-alig-c {
    text-align: center;
}

/* виджет с вопросами */
.left {
    display: flex;
    flex-direction: column;
}

.vid {
    background-color: #EEF1F4;
    padding: 10px;
    display: flex;
    justify-content: space-between;
    border-radius: 15px;
    margin-bottom: 10px;
    margin: 0 20% 15px 20%;
}

.vid:last-child {
    margin-bottom: 0;
}

/* общее расположение элементов */

.right {
    display: flex;
    align-items: center;
}

.right-in {
    display: flexbox;
}

.right p {
    margin: 0;
    margin: 0;
    color: #AEB8BC;
    font-size: 20px;
    font-style: normal;
    font-weight: 500;
    line-height: normal;
}

/* расцветовка */
.light {
    color: #488D57
}

.middle {
    color: #D8A326;
}

.hard {
    color: #D9382E;
}

/* левая чать виджета */

/* Верх */
.top-1 {
    display: flex;
    gap: 20px;
    margin-bottom: 10px;
}

.top-1 p {
    margin: 0;
}

.t {
    vertical-align: middle;
    width: 10px;
    height: 10px;
}

/* серидина */
.mid-1 {
    display: flex;
    flex-wrap: wrap;

    font-size: 28px;
    width: 100%;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    display: inline-block;
}

.mid-1 p {
    margin: 0;
    text-wrap: wrap;
}

.name-limit {
    width: 44ch;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}

/* низ */
.bottom-1 {
    display: flex;
    font-size: 15px;
    color: #AEB8BC;
}

.el {
    border-right: 1px solid #AEB8BC;
    padding: 7px;
}

.el-d {
    border-right: none;
    padding: 7px;
}

.-d {
    border-right: none;
}

.el p {
    margin: 0;
}


/* анимация */
div.vid {
    transition: all 0.5s;
}

div.vid:hover {
    transform: translateY(-10px);
    box-shadow: 10px 5px 5px rgb(0, 0, 0, 0.5);
}

/* Адаптивка */

@media(max-width: 1505px) {
    .mid-1 p {
        width: 100%;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        display: inline-block;
        text-overflow: ellipsis;
    }

    .mid-1 {
        width: 85%;
    }

    .left {
        width: 75%;
    }
}

@media(max-width: 1200px) {
    .q {
        font-size: var(--size-20);
    }
}

@media(max-width: 992px) {
    .q {
        font-size: var(--size-18);
    }

    .quest {
        margin: 0 15%;
    }

    .mid-1 p {
        font-size: 24px;
    }

}

@media(max-width: 910px) {
    .name-limit {
        width: 17ch;
    }

}

@media(max-width: 576px) {
    .q {
        font-size: var(--size-18);
    }

    .quest {
        margin: 0 15%;
    }

    .mid-1 p {
        font-size: var(--size-20);
    }

    .bottom-1 {
        font-size: 13px;
    }

    .right p {
        font-size: var(--size-18);
    }

    .imp-1 {
        padding-top: 13px;
    }
}

@media(max-width: 768px) {
    .q {
        font-size: var(--size-18);
    }

    .quest {
        margin: 0 15%;
    }

    .mid-1 p {
        font-size: var(--size-20);
    }

    .bottom-1 {
        font-size: 13px;
    }

    .right p {
        font-size: var(--size-18);
    }

    .imp-1 {
        padding-top: 13px;
    }
}

@media(max-width: 540px) {
    .vid {
        flex-direction: column;
    }
}

@media(max-width: 500px) {
    .vid {
        margin: 0;
        margin-bottom: 5px;
    }
}

@media(max-width: 400px) {
    .bottom-1 {
        flex-direction: column;
    }

    .el {
        width: 100px;
        border-right: none;
        border-bottom: 1px solid #AEB8BC;
    }

    .el:last-child {
        margin-bottom: 10px;
    }
}
</style>