<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="mookata fix"/>
        <attribute name="authors" value="Theerapong-PC01"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-16 06:30:41 PM"/>
        <attribute name="created" value="VGhlZXJhcG9uZy1QQzAxO0RFU0tUT1AtVFFCNTFHRTsyNTY4LTA3LTE2OzA2OjE5OjE4IFBNOzM2ODY="/>
        <attribute name="edited" value="VGhlZXJhcG9uZy1QQzAxO0RFU0tUT1AtVFFCNTFHRTsyNTY4LTA3LTE2OzA2OjMwOjQxIFBNOzE7Mzc4Mw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="total" type="Real" array="False" size=""/>
            <declare name="children, adults" type="Integer" array="False" size=""/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;-Child- 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;-Adult- 180 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="children"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="adults"/>
            <assign variable="total" expression="(children*120)+(adults*189)"/>
            <output expression="&quot;You ordered&quot; &amp; children &amp; &quot;children and&quot; &amp; adults &amp; &quot;adults&quot;" newline="True"/>
            <output expression="&quot;Total price:&quot; &amp; total &amp; &quot;Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>