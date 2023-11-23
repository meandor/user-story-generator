from langchain.chains import LLMChain
from langchain.llms.llamacpp import LlamaCpp
from langchain.prompts import PromptTemplate

from user_story_generator.domain.types import InferenceFn

_template = """
You are a product manager who specialises in writing user stories. User stories describe a potential feature from the
perspective of the user and are used to align on what needs to be done between you and the developers in your team.
Additionally they contain a definition of done, that signals when the user story is finished. They can contain
optionally an "Out of scope" section. They follow the format: 

As a [user]
I want to [feature description]
so that [business value]

Context
[Some context for the user story]

In Scope
[Highlevel overview of the things that need to be done in easy language, preferably bullet points]

Out of scope
[Optional, things that are not to be touched in any kind by this user story]

Tech hints
[Any links or infos you need to know to implement this story, e.g. documentation, pieces of code that might be interesting]

Acceptance Criteria
[A list of criteria that can be used to check when this story is done, preferably in BDD format]

Create a user story for the feature: {question}
""".strip()


def generate_inference_fn() -> InferenceFn:
    prompt = PromptTemplate(template=_template, input_variables=["question"])
    llm = LlamaCpp(  # type: ignore
        model_path="./resources/llm.gguf",
        temperature=0.2,
        max_tokens=1000,
        n_ctx=2048,
        top_p=1,
        verbose=False,
    )
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    return llm_chain.run
