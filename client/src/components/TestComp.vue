<script>
import axios from "axios";
export default {
  data() {
    return {
      form: {
        avatar: "",
        formdata: null,
      },
      link: null,
      formdata: null,
      data: null,
      isUploading: true,
      percentCompleted: 0,
      isLoading: false,
      l: {
        1: {
          convert: "Файл незагружен.",
          class: "notdownload",
        },
        2: {
          convert: "Файл незагружен.",
          class: "notdownload",
        },
      },
    };
  },
  methods: {
    async sendAvatar() {
      this.isLoading = true;
      this.isUploading = true;
      try {
        let res = await axios.post(
          "/test",
          this.formdata,
          {
            headers: {
              "Content-Type": "enctype=multipart/form-data",
            },
            onUploadProgress: (progressEvent) => {
              this.percentCompleted = Math.round(
                (progressEvent.loaded * 100) / progressEvent.total
              );
            },
          },
          
          
        );
        this.isLoading = true;
        this.link = res.data.res;
      } catch (err) {
        console.log("Ошибка отправки данных", err);
        this.isUploading = false;
        return;
        this.isLoading = false;
      }

      this.isUploading = false;
    },
    async convertFileAvatar(event, name) {
      const file = event.target.files[0];
      this.form.avatar = file;
      console.log(this.form.avatar);
      const reader = new FileReader();
      reader.onload = (e) => {
        this.form.avatar = e.target.result;
        console.log(this.form.avatar);
      };

   

      console.log(this.formdata);
    },
  },
  mounted() {
    console.log(this.l["1"].class);
    this.formdata = new FormData();
  },
};
</script>
<template>
  {{ this.percentCompleted }}
  {{ this.isLoading }}
  {{ this.form.avatar }}
  <form @submit.prevent="sendAvatar()">
    <input
      type="file"
      class="form-control mt-5"
      id="exampleFormControlInput1"
      placeholder="name@example.com"
      @change="convertFileAvatar($event, '1')"
    />

    <input
      type="file"
      class="form-control mt-5"
      id="exampleFormControlInput1"
      placeholder="name@example.com"
      @change="convertFileAvatar($event, '2')"
    />

    <button type="submit" class="btn btn-primary mt-2">Отправить</button>
    <a :href="this.link" class="link mt-5">{{ this.link }}</a>

    <div class="mb-3" v-if="isLoading">
      <label for="exampleFormControlInput1" class="form-label mt-3"
        ><h5>Загрузка данных на сервер...</h5></label
      >
      <progress
        max="100"
        :value="this.percentCompleted"
        v-if="this.isUploading"
      ></progress>
      <p>{{ this.percentCompleted }} %</p>
    </div>
  </form>
</template>

<style scoped>
.link {
  font-size: 50px;
}
</style>
