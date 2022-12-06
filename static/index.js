let cursor = 0;
const RANGE = 5;
const LIMIT = 16_000;

const translateText = async (question, keywords) => {
  const inferResponse = await fetch(`essays?question==${question}&keywords==${keywords}`);
  const inferJson = await inferResponse.json();

  return inferJson['generated_text'];
};

const textGenForm = document.querySelector(".text-gen-form");

textGenForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const textGenInput = document.getElementById("text-gen-input");
  const textGenKeyword = document.getElementById("text-gen-keyword");
  const textGenParagraph = document.querySelector(".text-gen-output");

  try {
    textGenParagraph.textContent = await translateText(
      textGenInput.value,
      textGenKeyword.value
    );
  } catch (err) {
    console.error(err);
  }
});