<template>
  <div>
    <div class="container">
      <span class="input-group-text">Izvođač i ime pjesme:</span>
      <input
        type="text"
        class="form-control"
        placeholder=""
        aria-label="Example text with button addon"
        aria-describedby="button-addon1"
        v-model="izvodac_ime_pjesme"
      />
      <span class="input-group-text">Url:</span>
      <input
        type="text"
        class="form-control"
        placeholder=""
        aria-label="Example text with button addon"
        aria-describedby="button-addon1"
        v-model="url"
      />
      <span class="input-group-text">Ocjena:</span>
      <input
        type="text"
        class="form-control"
        placeholder=""
        aria-label="Example text with button addon"
        aria-describedby="button-addon1"
        v-model="ocjena"
      />
      <span class="input-group-text">Piće:</span>
      <input
        type="text"
        class="form-control"
        placeholder=""
        aria-label="Example text with button addon"
        aria-describedby="button-addon1"
        v-model="pice"
      />
      <button
        v-on:click="posalji()"
        type="button"
        class="btn btn-dark"
        style="margin: 1em"
      >
        Upiši
      </button>

      <div class="container">
        <span class="input-group-text">Izvođač i ime pjesme:</span>
        <input
          type="text"
          class="form-control"
          placeholder=""
          aria-label="Example text with button addon"
          aria-describedby="button-addon1"
          v-model="izvodac_ime_pjesme"
        />

        <span class="input-group-text">Piće:</span>
        <input
          type="text"
          class="form-control"
          placeholder=""
          aria-label="Example text with button addon"
          aria-describedby="button-addon1"
          v-model="pice"
        />
        <button
          v-on:click="izbrisi()"
          type="button"
          class="btn btn-dark"
          style="margin: 1em"
        >
          Izbriši
        </button>
        <div>
          <button v-on:click="natrag" class="btn btn-dark" style="margin: 1em">
            Natrag
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      izvodac_ime_pjesme: "",
      url: "",
      ocjena: "",
      pice: "",
    };
  },
  mounted() {
    if (localStorage.ime) {
      this.izvodac_ime_pjesme = localStorage.getItem("izvodac_ime_pjesme");
      this.url = localStorage.getItem("url");
      this.ocjena = localStorage.getItem("ocjena");
      this.pice = localStorage.getItem("pice");
    }
  },
  methods: {
    posalji() {
      let xhr = new XMLHttpRequest();
      xhr.open("POST", "http://localhost:5000/upis");
      xhr.setRequestHeader("Accept", "application/json");
      xhr.setRequestHeader("Content-Type", "application/json");

      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
          console.log(xhr.status);
          console.log(xhr.responseText);
        }
      };

      let podatci = {
        ime: this.izvodac_ime_pjesme,
        url: this.url,
        ocjena: this.ocjena,
        pice: this.pice,
      };

      console.log(podatci);
      xhr.send(JSON.stringify(podatci));
    },

    izbrisi() {
      let xhr = new XMLHttpRequest();
      xhr.open("DELETE", "http://localhost:5000/delete");
      xhr.setRequestHeader("Accept", "application/json");
      xhr.setRequestHeader("Content-Type", "application/json");

      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
          console.log(xhr.status);
          console.log(xhr.responseText);
        }
      };

      let podatci = {
        ime: this.izvodac_ime_pjesme,
        url: this.url,
        ocjena: this.ocjena,
        pice: this.pice,
      };

      console.log(podatci);
      xhr.send(JSON.stringify(podatci));
    },

    natrag() {
      this.$router.push("/");
    },
  },
};
</script>
<style>
.form-control {
  width: 100%;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #212529;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ced4da;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  border-radius: 0.25rem;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}
</style>
