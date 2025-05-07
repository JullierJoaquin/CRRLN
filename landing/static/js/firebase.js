const firebaseConfig = {
  apiKey: "TU_API_KEY",
  authDomain: "TU_AUTH_DOMAIN",
  projectId: "TU_PROJECT_ID",
};

firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();

function login() {
  const provider = new firebase.auth.GoogleAuthProvider();
  auth.signInWithPopup(provider)
    .then((result) => result.user.getIdToken())
    .then((idToken) => {
      fetch('/verify-token', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ idToken })
      }).then(res => {
        if (res.ok) window.location.href = "/presupuestos";
        else alert("Error verificando token.");
      });
    })
    .catch((error) => {
      console.error(error);
      alert("Error de login");
    });
}
