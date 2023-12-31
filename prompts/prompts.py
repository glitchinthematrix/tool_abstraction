
#5 shot prompt

def generate_concept_recursion_prompt(input,parent):
    if parent is None:
        concept_recursion_prompt ='''
                    You are a helpful, enthusiastic assistant that describes the appearance of everyday things. Your response should be a detailed single-line description without mentioning the object. Additionally annotate, physical objects with <object> </object> 
                    
                    Input: Describe a chair
                    Answer: A sturdy, wooden <object>four-legged</object> seat with a slightly curved <object>backrest</object>, upholstered in soft fabric, and featuring a wide, contoured <object>flat surface</object> for comfortable sitting.

                    Input: Describe a microwave
                    Answer: An efficient, stainless steel rectangular <object>metal box</object> with a hinged <object>glass door</object>, complemented by a user-friendly <object>digital display</object> and a variety of buttons on the sleek <object>control panel</object>.

                    Input: Describe a sneaker
                    Answer: High-quality <object>lace-up</object> athletic footwear crafted with a durable <object>rubber sole</object>, a cushioned <object>collar</object> and tongue for added support, and stylish <object>logo</object> detailing on both the sides and tongue.

                    Input: Describe a sweater
                    Answer: A cozy, hand-knitted woolen garment featuring intricate cable patterns, long <object>snug-fitting sleeves</object>, a soft ribbed <object>crew neck</object>, and a comfortable, slightly loose fit for warmth and style.

                    Input: Describe a {input}
                    Answer:
                '''.format(input=input)
    else:
        concept_recursion_prompt ='''
        You are a helpful, enthusiastic assistant that describes the appearance of everyday things. Your response should be a detailed single-line description without mentioning the object. Additionally annotate, physical objects with <object> </object> 
                    
                    Input: Describe a chair
                    Answer: A sturdy, wooden <object>four-legged</object> seat with a slightly curved <object>backrest</object>, upholstered in soft fabric, and featuring a wide, contoured <object>flat surface</object> for comfortable sitting.

                    Input: Describe a microwave
                    Answer: An efficient, stainless steel rectangular <object>metal box</object> with a hinged <object>glass door</object>, complemented by a user-friendly <object>digital display</object> and a variety of buttons on the sleek <object>control panel</object>.

                    Input: Describe a sneaker
                    Answer: High-quality <object>lace-up</object> athletic footwear crafted with a durable <object>rubber sole</object>, a cushioned <object>collar</object> and tongue for added support, and stylish <object>logo</object> detailing on both the sides and tongue.

                    Input: Describe a sweater
                    Answer: A cozy, hand-knitted woolen garment featuring intricate cable patterns, long <object>snug-fitting sleeves</object>, a soft ribbed <object>crew neck</object>, and a comfortable, slightly loose fit for warmth and style.

                    Input: Describe a {input} of a {parent}
                    Answer:
                    '''.format(input=input,parent=parent)
        
    return concept_recursion_prompt

