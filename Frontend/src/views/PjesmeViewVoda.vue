<template>
  <div id="app">
    <LazyYoutube
      ref="youtubeLazyVideo"
      :src="youtubelinks[brojilo].url"
      max-width="720px"
      aspect-ratio="16:9"
      thumbnail-quality="standard"
    />

    <div class="col d-flex justify-content-center">
      <div class="card">
        <div>
          <div>
            <span class="text-center" style="margin: 1em"
              >Ime pjesme i izvođač: {{ youtubelinks[brojilo].ime }}</span
            >
          </div>
          <div>
            <span class="text-center" style="margin: 1em"
              >Alterrnativni link: {{ youtubelinks[brojilo].url }}</span
            >
          </div>
          <div>
            <span class="text-center" style="margin: 1em"
              >Ocjena kompatibilnosti: {{ youtubelinks[brojilo].ocjena }}</span
            >
          </div>
        </div>
      </div>
    </div>

    <div class="col d-flex justify-content-center">
      <div class="card">
        <div class="buttons">
          <button @click="prev()" class="btn btn-dark" style="margin: 1em">
            Prev
          </button>
          <button
            @click="handleClick('playVideo', 'youtubeLazyVideo')"
            class="btn btn-success"
            style="margin: 1em"
          >
            Play
          </button>
          <button
            @click="handleClick('stopVideo', 'youtubeLazyVideo')"
            class="btn btn-danger"
            style="margin: 1em"
          >
            Stop
          </button>
          <button
            @click="handleClick('pauseVideo', 'youtubeLazyVideo')"
            class="btn btn-warning"
            style="margin: 1em"
          >
            Pause
          </button>
          <button @click="next()" class="btn btn-dark" style="margin: 1em">
            Next
          </button>
        </div>
      </div>
    </div>

    <div class="col d-flex justify-content-center">
      <div class="card">
        Ocjenite pjesmu:
        <button-group class="text-center">
          <button
            class="btn btn-dark"
            @click="posalji(1)"
            style="margin: 0.2em"
          >
            1
          </button>
          <button
            class="btn btn-dark"
            @click="posalji(2)"
            style="margin: 0.2em"
          >
            2
          </button>
          <button
            class="btn btn-dark"
            @click="posalji(3)"
            style="margin: 0.2em"
          >
            3
          </button>
          <button
            class="btn btn-dark"
            @click="posalji(4)"
            style="margin: 0.2em"
          >
            4
          </button>
          <button
            class="btn btn-dark"
            @click="posalji(5)"
            style="margin: 0.2em"
          >
            5
          </button>
        </button-group>
        Dodajte komentar
        <input
          type="text"
          class="form-control"
          placeholder=""
          aria-label="Example text with button addon"
          aria-describedby="button-addon1"
          v-model="komentar"
        />

        <button
          class="btn btn-dark"
          @click="posalji_komentar"
          style="margin: 0.2em"
        >
          Pošalji komentar
        </button>
      </div>
    </div>
    <button v-on:click="natrag" class="btn btn-dark" style="margin: 0.2em">
      Natrag na odabir pića
    </button>
  </div>
</template>

<script>
import { LazyYoutube } from "vue-lazytube";

export default {
  name: "App",
  components: {
    LazyYoutube,
  },
  data() {
    return {
      youtubelinks: [{ url: "" }],
      brojilo: 0,
    };
  },

  async mounted() {
    let podatci = await fetch("http://localhost:5000/getanje/voda");
    let rezultati = await podatci.json();
    this.commits = rezultati;
    console.log(rezultati);
    this.youtubelinks = rezultati;
  },
  methods: {
    prev() {
      if (this.brojilo == 0) {
        this.brojilo = this.youtubelinks.length - 1;
      } else {
        this.brojilo -= 1;
      }
    },

    next() {
      if (this.brojilo == this.youtubelinks.length - 1) {
        this.brojilo = 0;
      } else {
        this.brojilo += 1;
      }
    },

    handleClick(event, ref) {
      this.$refs[ref][event]();
    },
    posalji(ocjena) {
      let xhr = new XMLHttpRequest();
      xhr.open("PATCH", "http://localhost:5000/izmjena");
      xhr.setRequestHeader("Accept", "application/json");
      xhr.setRequestHeader("Content-Type", "application/json");

      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
          console.log(xhr.status);
          console.log(xhr.responseText);
        }
      };

      let podatci = {
        ocjena: ocjena,
        url: this.youtubelinks[this.brojilo].url,
        pice: "Voda",
      };

      console.log(podatci);
      alert("Odabrana ocjena je: " + ocjena);
      xhr.send(JSON.stringify(podatci));
    },

    posalji_komentar() {
      let xhr = new XMLHttpRequest();
      xhr.open("POST", "http://localhost:5000/upis_komentara");
      xhr.setRequestHeader("Accept", "application/json");
      xhr.setRequestHeader("Content-Type", "application/json");

      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
          console.log(xhr.status);
          console.log(xhr.responseText);
        }
      };

      let podatci = {
        komentar: this.komentar,
        ime: this.youtubelinks[this.brojilo].ime,
        url: this.youtubelinks[this.brojilo].url,
        pice: "Voda",
      };

      console.log(podatci);
      alert("Vaš komentar je zabilježen.");
      xhr.send(JSON.stringify(podatci));
    },

    natrag() {
      this.$router.push("/about");
    },
  },
};
</script>
