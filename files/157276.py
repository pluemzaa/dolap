<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="2"/>
        <attribute name="authors" value="Nattakrit"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 02:03:02 PM"/>
        <attribute name="created" value="TmF0dGFrcml0O0xBUFRPUC1BTEVaRTsyMDI1LTA3LTE3OzAxOjQwOjQxIFBNOzMxMDI="/>
        <attribute name="edited" value="TmF0dGFrcml0O0xBUFRPUC1BTEVaRTsyMDI1LTA3LTE3OzAyOjAzOjAyIFBNOzE7MzIwNw=="/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="m, i, y, o" type="Real" array="False" size=""/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="m"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="y"/>
            <assign variable="o" expression="0"/>
            <while expression="o&lt;y">
                <assign variable="m" expression="m*(1+i*0.01)"/>
                <assign variable="o" expression="o+1"/>
                <output expression="&quot;Year &quot;&amp;o&amp;&quot;: &quot;&amp;m" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>