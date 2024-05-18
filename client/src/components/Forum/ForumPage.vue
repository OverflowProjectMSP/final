<script>
import axios from 'axios';
</script>

<template>
<div class="container d-flex flex-column gap-2 align-items-center">
    <h2 class="text-center mt-3">Выберите язык:</h2>
    <a href="/Forum?lang=javascript"><button class="btn btn-outline-primary">JavaScript</button></a>
    <a href="/Forum?lang=java"><button class="btn btn-outline-primary">Java</button></a>
    <a href="/Forum?lang=cs"><button class="btn btn-outline-primary">C#</button></a>
    <a href="/Forum?lang=python"><button class="btn btn-outline-primary">Python</button></a>
    <a href="/Forum?lang=php"><button class="btn btn-outline-primary">PHP</button></a>
    <a href="/Forum?lang=cpp"><button class="btn btn-outline-primary">C++</button></a>
    <a href="/Forum?lang=go"><button class="btn btn-outline-primary">Go</button></a>
    <a href="/Forum?lang=ruby"><button class="btn btn-outline-primary">Ruby</button></a>
    <a href="/Forum?lang=kotlin"><button class="btn btn-outline-primary">Kotlin</button></a>
    <a href="/Forum?lang=typescript" class="a"><button class="btn btn-outline-primary">TypeScript</button></a>
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