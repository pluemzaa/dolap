<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="tor moo bu sha"/>
        <attribute name="authors" value="computer"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-16 04:20:29 PM"/>
        <attribute name="created" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MDA6MzggUE07MjU3Ng=="/>
        <attribute name="edited" value="Y29tcHV0ZXI7Q1AtQ09NOzIwMjUtMDctMTY7MDQ6MjA6MjkgUE07MzsyNjg4"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="Child, Adult, total" type="Integer" array="False" size=""/>
            <output expression="&quot;Price List:&quot;&amp;&#13;&#10;tochar(13)&amp;&quot;- Child - 120 Baht per person&quot;&#13;&#10;&amp;tochar(13)&amp;&quot;- Adult - 189 Baht per person&quot;" newline="True"/>
            <output expression="&quot;Enter number of children: &quot;" newline="True"/>
            <input variable="Child"/>
            <output expression="&quot;Enter number of adults: &quot;" newline="True"/>
            <input variable="Adult"/>
            <assign variable="total" expression="(Child * 120) + (Adult * 189)"/>
            <output expression="&quot;You ordered&quot;&amp; (Child) &amp;  &quot;children and&quot; &amp; (Adult) &amp;&quot;adults&quot;&#13;&#10;&amp; tochar(13) &amp;&quot;Total price:&quot;&amp; (total) &amp; &quot;Baht&quot;&#13;&#10;&amp; tochar(13) &amp;&quot;Enjoy your meal!&quot;" newline="False"/>
        </body>
    </function>
</flowgorithm>