<?xml version="1.0"?>
<flowgorithm fileversion="4.2">
    <attributes>
        <attribute name="name" value="flowchart &#3586;&#3657;&#3629; 3"/>
        <attribute name="authors" value="benzs"/>
        <attribute name="about" value=""/>
        <attribute name="saved" value="2025-07-17 04:31:50 PM"/>
        <attribute name="created" value="YmVuenM7REVTS1RPUC1FNDZHTjZKOzIwMjUtMDctMTc7MDQ6MTQ6MjQgUE07Mjg2NA=="/>
        <attribute name="edited" value="YmVuenM7REVTS1RPUC1FNDZHTjZKOzIwMjUtMDctMTc7MDQ6MzE6NTAgUE07MzsyOTcy"/>
    </attributes>
    <function name="Main" type="None" variable="">
        <parameters/>
        <body>
            <declare name="ns, ne" type="Real" array="False" size=""/>
            <output expression="&quot;Input start number: &quot;" newline="True"/>
            <input variable="ns"/>
            <output expression="&quot;Input end number: &quot;" newline="True"/>
            <input variable="ne"/>
            <while expression="ns&lt;=ne">
                <output expression="ns" newline="True"/>
                <assign variable="ns" expression="ns + 1"/>
            </while>
        </body>
    </function>
</flowgorithm>