<script>
export default {
  data() {
    return {
      
    }
  },

  methods: {
    async putInfo() {
      this.form.interestings = this.form.interestings.substr(0, 48);
      this.isLoading = true;
      this.isUploading = true; // Включаем индикатор загрузки
      try {
        await axios.put(
          "/user-info",
          {
            form: this.form,
          },
          {
            onUploadProgress: (progressEvent) => {
              const percentCompleted = Math.round(
                (progressEvent.loaded * 100) / progressEvent.total
              );
              this.percentCompleted = percentCompleted;
            },
          }
        );
        this.isUploading = true; // Выключаем индикатор загрузки
       // this.$router.push(`/Profile/${this.id}`)
      } catch (error) {
        console.error("Ошибка при отправке данных:", error);
        this.isUploading = false; // Выключаем индикатор загрузки
        // Добавьте обработку ошибки
      }
    },
  }
}
</script>

<template>
<form @submit.prevent="putInfo"> 
  <div class="window">
    <div class="change-block">
      <h1>Изменить пароль</h1>
      <div class="inputs">
        <div class="old-pass">
          <input type="password">
          <span>Старый пароль</span>  
        </div>
        <div class="new-pass">
          <input type="password">
          <span>Новый пароль</span>
        </div>
        <div class="res-pass">
          <input type="password">
          <span>Повторите пароль</span>
        </div>
        <div class="save">
          <button type="submit">Сохранить изменениия</button>
        </div>

      </div>
    </div>
  </div>
</form>
</template>

<style scoped>

.save {
  display: flex;
  justify-content: start;
  width: 100%;
}

.save button {
    background-color: rgb(255, 255, 255);
    font-size: 20px;
    font-weight: 500;
    color: #7ac97a;
    border: 2px solid #7ac97a;
    border-radius: 8px;
    width: 360px;
    text-align: center;
    transition: all 200ms;
    width: 300px;
    height: 40px;
}

.save button:hover {
  background-color: #7ac97a;
  color: #ffffff;
}

.save button:active {
  background-color: #5ba35b;
}

.window {
  width: 100%;
  height: 100vh;

  display: flex;
  justify-content: center;
}

.change-block {
  width: 60%;
}

.inputs {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 40px;
}

.inputs div {
  width: 70%;
}

input {
  width: 100% !important;

  width: 300px;
  height: 40px;
  border: 2px solid #000;
  background-color: #fff;
  border-radius: 8px;
  font-size: 20px;
  padding: 0 10px;
}

.change-block h1 {
  border-bottom: 2px solid #000;
  padding-bottom: 20px;
  font-size: 30px;
  margin-bottom: 50px;
}

.old-pass input {
 
}

.old-pass {
  position: relative;
}

.old-pass span {
  position: absolute;
  left: 10px;
  top: -22px;
  background-color: #3b82f6;
  padding: 1px 20px;
  color: #fff;
  font-size: 18px;
  font-weight: 500;
  border-radius: 8px;
}

.new-pass input {
  
}

.new-pass {
  position: relative;
}

.new-pass span {
  position: absolute;
  left: 10px;
  top: -22px;
  background-color: #3b82f6;
  padding: 1px 20px;
  color: #fff;
  font-size: 18px;
  font-weight: 500;
  border-radius: 8px;
}


.res-pass input {
}

.res-pass {
  position: relative;
}

.res-pass span {
  position: absolute;
  left: 10px;
  top: -22px;
  background-color: #3b82f6;
  padding: 1px 20px;
  color: #fff;
  font-size: 18px;
  font-weight: 500;
  border-radius: 8px;
}



















</style>
