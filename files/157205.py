<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="&#3650;&#3615;&#3594;&#3634;&#3605;BB"/>
        <attribute name="authors" value="BabyBest"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2568-07-21 09:47:36 PM"/>
        <attribute name="created" value="QmFieUJlc3Q7REVTS1RPUC00M0lESEZPOzI1NjgtMDctMjE7MDM6NDk6NDkgQU07MzExNw=="/>
        <attribute name="edited" value="QmFieUJlc3Q7REVTS1RPUC00M0lESEZPOzI1NjgtMDctMjE7MDk6NDc6MzYgUE07MzszMjQy"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <output expression="&quot;Price List:&quot;" newline="True"/>
            <output expression="&quot;-Child - 120 Baht per person&quot;" newline="True"/>
            <output expression="&quot;-Adult- 189 Baht per person&quot;" newline="True"/>
            <declare name="child" type="Integer" array="False" size=""/>
            <declare name="adult" type="Integer" array="False" size=""/>
            <declare name="Total" type="Integer" array="False" size=""/>
            <output expression="&quot;Enter number of children:&quot;" newline="True"/>
            <input variable="child"/>
            <output expression="&quot;Enter number of adults:&quot;" newline="True"/>
            <input variable="adult"/>
            <assign variable="Total" expression="(child*120)+(adult*189)"/>
            <output expression="&quot;You ordered&quot;&amp;child&amp;&quot; children and&quot;&amp; adult &amp;&quot;adults&quot;" newline="True"/>
            <output expression="&quot;total price: &quot;&amp; total &amp;&quot;Baht&quot;" newline="True"/>
            <output expression="&quot;Enjoy your meal!&quot;" newline="True"/>
        </body>
    </function>
</flowgorithm>