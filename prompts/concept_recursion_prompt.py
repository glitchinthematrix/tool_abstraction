
system_prompt = '''You are a helpful, enthusiastic assistant to the blind who
                 helps them understand the outward appearance of everyday objects. 
                 Your response should be a detailed single-line description without 
                 mention of the object itself'''

#5 shot prompt
user_prompt_5 = '''
            Input: Describe the appearance of a chair? 
            Answer: A furniture with a <object>backrest</object>, <object> seat</object> for sitting and sometimes an <object>armrest</object>
            Input: Describe the appearance of a smartphone?
            Answer: A handheld device with a <object>touchscreen</object> display, physical <object>buttons</object>, and a <object>camera</object> on the back.
            Input: Describe the appearance of a sweater?
            Answer: A garment made of knitted fabric, worn over the upper body with long or short <object>sleeves</object> and a <object>collar</object>.
            Input: Describe the appearance of a sneaker? 
            Answer: A type of footwear with a rubber <object>sole</object>, laced <object>upper</object>, and comfortable <object>cushioning</object>
            Input: Describe the appearance of a microwave?              
            Answer: A kitchen appliance with a <object>door</object>, digital <object>control panel</object>, and a <object>turntable</object> inside
            Input: Describe the appearance of a {input}?
            '''

#10 shot prompt
user_prompt_10 = '''
            Input: Describe the appearance of a chair?  
            Answer: A furniture with a <object>backrest</object>, <object> seat</object> for sitting and sometimes an <object>armrest</object>
            Input: Describe the appearance of a smartphone?
            Answer: A handheld device with a <object>touchscreen</object> display, physical <object>buttons</object>, and a <object>camera</object> on the back.
            Input: Describe the appearance of a sweater?
            Answer: A garment made of knitted fabric, worn over the upper body with long or short <object>sleeves</object> and a <object>collar</object>.
            Input: Describe the appearance of a sneaker?
            Answer: A type of footwear with a rubber <object>sole</object>, laced <object>upper</object>, and comfortable <object>cushioning</object>
            Input: Describe the appearance of a microwave?
            Answer: A kitchen appliance with a <object>door</object>, digital <object>control panel</object>, and a <object>turntable</object> inside
            Input: Describe the appearance of a table?
            Answer: A furniture with a <object>flat</object> <object>surface</object> supported by <object>legs</object>
            Input: Describe the appearance of a laptop?
            Answer: A portable computer with a <object>screen</object>, <object>keyboard</object>, and <object>trackpad</object>
            Input: Describe the appearance of a book?
            Answer: A rectangular object with <object>pages</object> bound together, often with a <object>cover</object> and <object>text</object> printed on the pages.
            Input: Describe the appearance of a car?
            Input: A vehicle with four <object>wheels</object>, a <object>windshield</object>, <object>doors</object> on each side, and a <object>license plate</object> on the rear.
'''
