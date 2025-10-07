<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="flowchart &#3586;&#3657;&#3629; 4"/>
        <attribute name="authors" value="benzs"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 05:05:31 PM"/>
        <attribute name="created" value="YmVuenM7REVTS1RPUC1FNDZHTjZKOzIwMjUtMDctMTc7MDQ6MzM6NDUgUE07Mjg2OA=="/>
        <attribute name="edited" value="YmVuenM7REVTS1RPUC1FNDZHTjZKOzIwMjUtMDctMTc7MDU6MDU6MzEgUE07MTsyOTcx"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="m, i, y, o" type="Real" array="False" size=""/>
            <assign variable="o" expression="0"/>
            <output expression="&quot;Input money:&quot;" newline="True"/>
            <input variable="m"/>
            <output expression="&quot;Input interest (%):&quot;" newline="True"/>
            <input variable="i"/>
            <output expression="&quot;Input years:&quot;" newline="True"/>
            <input variable="y"/>
            <while expression="o&lt;y">
                <assign variable="m" expression="m * (1 + (i/100))"/>
                <assign variable="o" expression="o + 1"/>
                <output expression="&quot;Year &quot;&amp;o&amp;&quot;:&quot;&amp;m" newline="True"/>
            </while>
        </body>
    </function>
</flowgorithm>