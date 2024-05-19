<script>
export default {
    props: {
        Show: Boolean,
        title: String,
    },
    methods: {
        CloseModal() {
            this.$emit('CloseModal', this.Show)
          
        }
    }
}
</script>

<template>
    <div class="modal-backdrop">
        <div class="window">
            <div class="close">
                <button class="btn-close" @click="CloseModal">X</button>
            </div>
            <h3>Что вы хотите сделать?</h3>
            <div class="buttons">
                <form action="/NewState">
                    <button class="btn" href="#/Main">Создать статью</button>
                </form>
                <form action="/NewQuetion">
                    <button class="btn">Создать вопрос</button>
                </form>
            </div>
        </div>
    </div>

</template>

<style scoped>
.window {
    background-color: #ffffff;
    border: 4px solid #2a2a2a;
    width: 500px;
    height: 300px;
    border-radius: 30px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 50px;

    position: relative;

    font-family: "Rubik", sans-serif;
    user-select: none;
}

.btn {
    width: 170px;
    height: 50px;
    border-radius: 12px;
    border: none;
    background-color: #4200FF;
    color: #fff;
    cursor: pointer;
    font-weight: 600;
    font-size: 16px;

    transition: all 100ms;
}

.btn:hover {
    background-color: #2d00aa;
    border-radius: 25px 5px;
}

.btn:active {
    background-color: #240088;
}

.buttons {
    display: flex;
    gap: 20px;
}

.close {
    width: 50px;
    height: 50px;
    background-color: #2a2a2a;
    position: absolute;
    top: 0;
    right: 0;
    border-radius: 0px 16px 0px 16px;

    display: flex;
    justify-content: center;
    align-items: center;

    transition: all 100ms;
}

.close:hover {
    background-color: #1a1a1a;
    border-radius: 0px 16px 0px 25px;
}

.close:active {
    background-color: #111111;
}

.btn-close {
    width: 50px;
    height: 50px;
    border-radius: 16px;
    background: none;
    border: none;
    color: #fff;
    font-size: 22px;
    font-weight: 500;

    cursor: pointer;
}

.modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>