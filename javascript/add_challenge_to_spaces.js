//Import dependcies
import fs from "fs";
import YAML from "js-yaml";

//import actions
import postQuestion from "./js_actions.js";

try {
	const raw = fs.readFileSync("././topics.yaml");
	const data = YAML.load(raw);
	const lengthOfYAMLfile = Object.values(data).length;
	const latestQuestion = data[lengthOfYAMLfile];
	postQuestion(latestQuestion, lengthOfYAMLfile);
} catch (err) {
	console.log(err);
}
