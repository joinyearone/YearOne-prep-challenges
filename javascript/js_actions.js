import fetch from "node-fetch";

const API_TOKEN = process.env.API_TOKEN;
const COMMUNITY_ID = process.env.COMMUNITY_ID;
const CIRCLE_COMMUNITY_PATH = process.env.CIRCLE_COMMUNITY_PATH;
const BEGGINER_SPACE_ID = process.env.BEGGINER_SPACE_ID;
const MEDIUM_SPACE_ID = process.env.MEDIUM_SPACE_ID;
const ADVANCED_SPACE_ID = process.env.ADVANCED_SPACE_ID;

const postQuestion = async (question, questionNumber) => {
	const { title, difficulty, source, body, author_name } = question;

	const requestOptions = {
		method: "POST",
		headers: { Authorization: API_TOKEN },
	};

	const questionDifficulties = {
		Beginner: BEGGINER_SPACE_ID,
		Medium: MEDIUM_SPACE_ID,
		Advanced: ADVANCED_SPACE_ID,
	};

	const SPACE_ID = questionDifficulties[difficulty];

	//post sections
	let titleHTML = `Interview Prep Challenge ${questionNumber}: ${title}`;
	let bodyHTML = `
    👏👏 <h3>Thanks to <u>${author_name}</u> for the question!👏👏</h3><br>
    <br>
    <strong>Difficulty Level:</strong> ${difficulty}<br>
    <strong>Sourced from:</strong> ${source}<br>
    <br>
    ${body} <br>
    <br>
    This question was submitted in the YearOne Open Source project, to submit a topic, go to github.com/YearOne-Prep/YearOne-prep-challenges
    <br><br>
    Don't forget to let us know that you've completed this question!
    Leave a comment below 👇👇👇👇
  `;

	//url creation
	const url = encodeURI(formatPostBody(titleHTML, bodyHTML));

	function formatPostBody(titleSection, bodySection) {
		const post_url = `${CIRCLE_COMMUNITY_PATH}/api/v1/posts?community_id=${COMMUNITY_ID}&SPACE_ID=${SPACE_ID}&`;
		const post_title = `name=${titleSection}&`;
		const post_body = `internal_custom_html=${bodySection}&`;
		const post_url_ending_params = `is_comments_enabled=true&is_liking_enabled=true&is_truncation_disabled=false`;

		const url_pieces = [
			post_url,
			post_title,
			post_body,
			post_url_ending_params,
		];

		return url_pieces.join("");
	}

	await fetch(url, requestOptions)
		.then((response) => response.json())
		.then((result) => {
			console.log(result);
		})
		.catch((error) => console.log("error", error));
};

export default { postQuestion };
