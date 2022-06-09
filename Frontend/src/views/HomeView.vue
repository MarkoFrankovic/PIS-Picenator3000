<template>
  <div>
    <div>
      <div>
        <i>
          <div>
            <div>
              <h1>Pičenator 3000</h1>
              <hr class="w3-border-grey" style="margin: auto; width: 100%" />
            </div>
            <button
              v-on:click="korisnik"
              type="button"
              class="btn btn-outline-light"
              style="margin: 0.5em"
            >
              Pičenator
            </button>

            <button
              v-on:click="login"
              type="button"
              class="btn btn-outline-light"
              style="margin: 0.5em"
            >
              Upis
            </button>
          </div>
        </i>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      brojilo: 0,
    };
  },

  methods: {
    login() {
      this.$router.push("/admin");
    },
    korisnik() {
      this.$router.push("/about");
    },
  },
};
</script>

<style>
body,
.center {
  display: flex;
  justify-content: center;
  align-items: center;
}

i {
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: "Inter", inter;
  color: whitesmoke;
  outline-color: rgb(92, 92, 92);
  height: 0.1px;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  margin: auto;
  background-image: url("@/assets/img/thumbnail.jpg");
  background-repeat: no-repeat;
  background-size: 100%;
  width: 100%;
  height: 100%;
}

body,
html {
  min-height: 100%;
  min-width: 100%;
}
</style>
