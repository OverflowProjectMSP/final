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
      l: {
        "1": {
          convert: "Файл незагружен.",
          class: "notdownload",
        },
        "2": {
          convert: "Файл незагружен.",
          class: "notdownload",
        }
      }
    };
  },
  methods: {
    async sendAvatar() {
      const config = {
        headers: {
          "Content-Type": "enctype=multipart/form-data",
        },
      };


       let res = await axios.post("/test", this.formdata, {
            headers: {
                "Content-Type": "enctype=multipart/form-data",
            },
       })
          this.link = res.data.res
        this.formdata = new FormData()
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
    
        this.formdata.append(name, file)    
      
     
      console.log(this.formdata);
    },
  },
  mounted() {
    console.log(this.l["1"].class)
   this.formdata = new FormData(); 
  },
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
  </form>
</template>

<style scoped>
.link {
  font-size: 50px;
}
</style>
