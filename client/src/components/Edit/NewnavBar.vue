<script>

</script>

<template>
    <div class="navbar">
        <div class="items">
            <div class="icon-img">
                <a href=""><img src="../../assets/Main/uflogo.svg" alt=""></a>
                <a href=""><h2>UpFollow</h2></a>
            </div>
            <a href="">Вопросы</a>
            <a href="">Статьи</a>
            <a href="">Форум</a>
            <a href="">Новости IT</a>
        </div>
        <div class="enter">           
            <button class=""><span>Войти</span></button>
            <a class="d-none" href=""><img src="../../assets/Main/hebber.png" alt=""></a>
        </div>
    </div>
</template>

<style>
.navbar {

    display: flex;
    justify-content: space-between;
    align-items: center;


    padding: 0 30px 0 30px;

    border-radius: 14px;
    width: 97%;
    min-height: 70px !important;

    background-color: rgba(59, 130, 246, 0.8)

    
}


.items {
    display: flex;
    align-items: center;
    gap: 50px;
}

.items img {
    width: 50px;
    margin-bottom: 8px;

}

.items a {
    color: #fff;
    font-size: 18px;
    font-weight: 500;
    transition: 200ms;

}

.items a:hover {
    opacity: 0.7;
}

h2 {
    margin: 0;
    color: #fff;
    font-size: 24px;
    font-weight: 600;
}

.icon-img {
    display: flex;
    align-items: center;
    gap: 15px;


    border-right: 2px solid #fff;
    
    padding-right: 30px;
}

.icon-img a:hover {
    opacity: 0.8 !important;
}

.enter button{
    width: 120px;
    border-radius: 5px;
    color: #000;   
    background-color: #fff;
  line-height: 42px;
  padding: 0;
  border: none;
  position: relative;
  font-weight: 500;
  transition: background-color 300ms ease;
}
.enter button span {
  position: relative;
  display: block;
  width: 100%;
  height: 100%;
}
.enter button:before,
.enter button:after {
  position: absolute;
  content: "";
  right: 0;
  bottom: 0;
  background-color: #fff;
 
  transition: all 300ms ease;
}
.enter button:before{
   height: 0%;
   width: 2px;
}
.enter button:after {
  width: 0%;
  height: 2px;
}
.enter button:hover{
  color: #fff;
  background-color: #3d72d3;
}
.enter button:hover:before {
  height: 100%;

}
.enter button:hover:after {
  width: 100%;
}
.enter button span:before,
.enter button span:after {
  position: absolute;
  content: "";
  left: 0;
  top: 0;
  background-color: #fff;
  transition: all 300ms ease;
}
.enter button span:before {
  width: 2px;
  height: 0%;
}
.enter button span:after {
  height: 2px;
  width: 0%;
}
.enter button span:hover:before {
  height: 100%;
}
.enter button span:hover:after {
  width: 100%;
}


.enter img {
    width: 60px;
    border-radius: 10px;
    transition: 200ms;
}

.enter img:hover {
    filter: brightness(85%);
}

</style>
















