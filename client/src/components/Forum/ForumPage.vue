<script>
import axios from 'axios';
</script>

<template>
<div class="container d-flex flex-column gap-2 align-items-center">
    <h2 class="text-center mt-3">Выберите язык:</h2>
    <a href="/Forum?lang=Javascript"><button class="btn btn-outline-primary">JavaScript</button></a>
    <a href="/Forum?lang=Java"><button class="btn btn-outline-primary">Java</button></a>
    <a href="/Forum?lang=Cs"><button class="btn btn-outline-primary">C#</button></a>
    <a href="/Forum?lang=Python"><button class="btn btn-outline-primary">Python</button></a>
    <a href="/Forum?lang=Php"><button class="btn btn-outline-primary">PHP</button></a>
    <a href="/Forum?lang=Cpp"><button class="btn btn-outline-primary">C++</button></a>
    <a href="/Forum?lang=Go"><button class="btn btn-outline-primary">Go</button></a>
    <a href="/Forum?lang=Ruby"><button class="btn btn-outline-primary">Ruby</button></a>
    <a href="/Forum?lang=Kotlin"><button class="btn btn-outline-primary">Kotlin</button></a>
    <a href="/Forum?lang=Typescript" class="a"><button class="btn btn-outline-primary">TypeScript</button></a>
</div>  
</template>

<style scoped>
.a{
    margin-bottom: 30px;
}
a, button {
    width: 320px !important;
}
</style>