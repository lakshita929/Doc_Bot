from gpt4all import GPT4All


class LLM:
    def __init__(self, config):
        self.config = config
        self.model = GPT4All(self.config.model_name, device=self.config.device)
        self.prompt_template = open(self.config.prompt_template_path).read()
        self.system_template = open(self.config.system_template_path).read()
        
    def _get_prompt(self):
        prompt_text = input('Question:  ')
        return prompt_text.strip()
    
    def _post_answer(self, answer):
        print(f'Answer: {answer}')
        
    def chat_session(self, embed_db, kb):
        self.keep_chatting = True
        while self.keep_chatting:
            with self.model.chat_session(self.system_template):
                prompt_text = self._get_prompt()
                
                context = embed_db.query(kb, prompt_text)
                
                prompt = f'Context: {context} \n\nQuestion: {prompt_text}\n\n'
                
                answer = self.model.generate(
                    prompt, 
                    max_tokens=self.config.max_gen_tokens,
                    temp=self.config.temparature,
                    top_k=self.config.top_k,
                    top_p=self.config.top_p,
                    repeat_penalty=self.config.repeat_penalty,
                    repeat_last_n=self.config.repeat_last_n,
                    streaming=self.config.streaming,
                    
                )
                
                if self.config.streaming:
                    for token in answer:
                        print('Do Something With The Token')
                        print(token)
                        
                else:
                    self._post_answer(answer)

            if prompt == 'exit()':
                self.keep_chatting = False
                break