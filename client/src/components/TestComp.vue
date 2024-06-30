<script>
import axios from "axios";
export default {
  data() {
    return {
      form: {
        avatar: "",
        filename: "",
        formdata: null,
      },
      link: null,
    };
  },
  methods: {
    async sendAvatar() {
      const config = {
        headers: {
          "Content-Type": "enctype=multipart/form-data",
        },
      };

        const form = new FormData();
        form.append("file", this.form.avatar);

        axios.post("/test", form, {
            headers: {
                "Content-Type": "enctype=multipart/form-data",
            },
          })
          .then((response) => {
            console.log(response.data);
          })
          .catch((error) => {
            console.error(error);
          });
    },
    async convertFileAvatar(event) {
      const file = event.target.files[0];
      this.form.avatar = file;
      const filename = event.target.files[0].name;
      console.log(this.form.avatar);
      //   console.log(this.form.avatar);
    //   const reader = new FileReader();
      this.form.filename = filename;
    //   reader.onload = (e) => {
    //     this.form.avatar = e.target.result;
    //     console.log(this.form.avatar);
    //   };
    //   reader.readAsArrayBuffer(file);

      const formdata = new FormData(); // Добавляем файл в FormData. file должен быть объектом File, который можно получить, например, через input type="file" formData.append('file', file); // Настраиваем запрос const config = { headers: { 'Content-Type': 'multipart/form-data' // Это важно, так как мы отправляем файл } }; // Делаем POST-запрос с файлом
      this.formdata = formdata.append("file", file);
      console.log(this.formdata); // это undefined будет
    },
  },
  mounted() {},
};
</script>
<template>
  {{ this.form.avatar }}
  <form @submit.prevent="sendAvatar()">
    <input
      type="file"
      class="form-control mt-5"
      id="exampleFormControlInput1"
      placeholder="name@example.com"
      @change="convertFileAvatar"
    />

    <button type="submit" class="btn btn-primary mt-2">Отправить</button>
    <a :href="this.link" class="link mt-5">{{ this.link }}</a>
  </form>
</template>

<style scoped>
.link {
  font-size: 50px;
}
</style>
