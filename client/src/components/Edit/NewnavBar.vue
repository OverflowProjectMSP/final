<script>

</script>

<template>
    <div class="navbar">
        <div class="items">
            <div class="icon-img">
                <img src="../../assets/Main/uflogo.svg" alt="">
                <h2>UpFollow</h2>
            </div>
            <a href="">Вопросы</a>
            <a href="">Статьи</a>
            <a href="">Форум</a>
            <a href="">Новости IT</a>
        </div>
        <div class="enter">           
            <button class="d-none">Войти</button>
            <a class="" href=""><img src="../../assets/Main/hebber.png" alt=""></a>
        </div>
    </div>
</template>

<style>
.navbar {

    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 0 30px 0 30px;

    border-radius: 20px;
    width: 95%;
    min-height: 80px !important;

    background-color: rgba(59, 130, 246, 0.8)

    
}

.RouterView {
    min-height: 0 !important;
}

.items {
    display: flex;
    align-items: center;
    gap: 50px;
}

.items img {
    width: 70px;
    margin-bottom: 8px;

}

.items a {
    color: #fff;
    font-size: 20px;
    font-weight: 500;
}

h2 {
    margin: 0;
    color: #fff;
    font-weight: 600;
}

.icon-img {
    display: flex;
    align-items: center;
    gap: 15px;

    margin-right: 30px;
}

.enter {
}

.enter button {
    width: 130px;
    height: 50px;
    font-size: 20px;

    border: none;
    border-radius: 8px;

    background-color: #fff;
}

.enter img {
    width: 60px;
    border-radius: 10px;
}

</style>
















