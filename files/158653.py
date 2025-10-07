<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="Flow&#3586;&#3657;&#3629;1"/>
        <attribute name="authors" value="nitip"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-22 05:08:45 PM"/>
        <attribute name="created" value="bml0aXA7TVNJOzI1NjgtMDctMjI7MDQ6NTk6NTcgUE07MjA4Nw=="/>
        <attribute name="edited" value="bml0aXA7TVNJOzI1NjgtMDctMjI7MDU6MDg6NDUgUE07MTsyMTg3"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <output expression="&quot;Price List&quot;" newline="True"/>
            <output expression="&quot;-Child- 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;-Adult- 189 Baht per person&quot;" newline="True"/>
            <declare name="children" type="Integer" array="False" size=""/>
            <declare name="adults" type="Integer" array="False" size=""/>
            <declare name="total" type="Integer" array="False" size=""/>
            <output expression="&quot;Enter number of children: &quot;" newline="True"/>
            <input variable="children"/>
            <output expression="&quot;Enter number of adults: &quot;" newline="True"/>
            <input variable="adults"/>
            <assign variable="total" expression="(children * 120) + (adults * 189)"/>
            <output expression="&quot;You ordered &quot; &amp; children &amp; &quot; children and &quot; &amp; adults &amp;&quot; adults &quot;" newline="True"/>
            <output expression="&quot;Total price: &quot; &amp; total &amp; &quot; Baht &quot;" newline="True"/>
            <output expression="&quot;Enjoy you meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>