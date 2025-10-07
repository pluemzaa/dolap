<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="lab1"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 02:25:06 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6MDA6NTIgUE07MjU3MA=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDI6MjU6MDYgUE07MTsyNjg0"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="child, Adult, children, Adults, total" type="Integer" array="False" size=""/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="child"/>
            <assign variable="children" expression="child*120"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="Adult"/>
            <assign variable="Adults" expression="Adult*189"/>
            <output expression="&quot;Your ordered&quot;&amp;child&amp;&quot;children and&quot;&amp;Adult&amp;&quot;adults&quot;" newline="True"/>
            <assign variable="total" expression="children+Adults"/>
            <output expression="&quot;Total price:&quot;&amp;total" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>