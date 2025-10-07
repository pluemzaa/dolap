<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="&#3629;&#3619;&#3656;&#3629;&#3618;&#3648;&#3621;&#3618;"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 06:32:27 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDU6NTU6NTYgUE07MjU4Nw=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDY6MzI6MjcgUE07MTsyNjg5"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="c, a, total" type="Integer" array="False" size=""/>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;- Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="c"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="a"/>
            <assign variable="total" expression="(c*120)+(a*189)"/>
            <output expression="&quot;You ordered&quot; &amp;c&amp; &quot;children and&quot; &amp;a&amp; &quot;adults&quot;" newline="True"/>
            <output expression="&quot;Total price:&quot; &amp;Total&amp; &quot;Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>